"""Self-debugging layer: the loop diagnoses and repairs its own failures.

When a proposal's diff won't apply or its solver crashes in grading, the
loop doesn't just revert — it classifies the error, makes ONE bounded
repair attempt with the coder seat, re-tests, and records the episode.
Every episode becomes a notebook finding, so the collective learns to
avoid (and fix) errors it has already seen: the system gets better at
debugging itself the longer it runs.

A circuit breaker (see controller.write_traj) stops the run after 6
consecutive reverted proposals — a stuck loop ends itself instead of
burning calls.
"""
import datetime
import fcntl
import json
import os
import re
import shutil
import sys
import tempfile

LOOP_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG_JOURNAL = os.path.join(LOOP_DIR, "journals", "debug.md")

sys.path.insert(0, LOOP_DIR)
from notebook import FINDINGS_PATH  # reuse the findings file for debug lessons

# error signature -> (category, auto_fixable, hint for the repair prompt)
PATTERNS = [
    (r"hunk .* failed|malformed patch|can't find file to patch|"
     r"only garbage was found|unexpected end of file in patch",
     "bad_diff", True,
     "Regenerate the diff against the EXACT current context lines shown. "
     "Keep context lines byte-identical."),
    (r"SyntaxError", "solver_syntax", True,
     "Fix the syntax error at the reported line. Change nothing else."),
    # FIX #3 (Opus review 2026-10-09): the bare "Traceback" pattern used to
    # precede the infra patterns, so "…429" / "TimeoutError" / "MemoryError"
    # inside a traceback misclassified as fixable solver_crash and burned a
    # coder call. Non-fixable infra patterns now come FIRST, and matching
    # scans the END of the text where tracebacks put the real cause.
    (r"timed out|timeout|TimeLimitExceeded", "timeout", False,
     "Infra flake, not a code bug. Retry later; do not burn calls on it."),
    (r"\b429\b|rate.?limit|quota|exhausted|\b403\b|\b1113\b|\b1305\b|"
     r"insufficient.*balance|overloaded",
     "quota", False,
     "Provider quota hit. Wait for the next rotation; do not retry now."),
    (r"FileNotFoundError|No such file or directory", "missing_file", False,
     "A file the code expects is absent. Check the diff touched the right paths."),
    (r"MemoryError|out of memory", "oom", False,
     "The solver used too much memory. Simplify before retrying."),
    # Genuine code crashes come LAST: only if no infra pattern matched.
    # The final exception line (e.g. "ValueError: …") is the signal; a bare
    # "Traceback" header alone is not.
    (r"Traceback \(most recent call last\)", "solver_crash", True,
     "Fix the crashing line. If the traceback points outside solver.py, "
     "say UNFIXABLE instead of a diff."),
]


def _final_exception_line(text):
    """Last 'XxxError: …' line — the real cause, per Opus fix #3."""
    lines = [l.strip() for l in (text or "").split("\n") if l.strip()]
    for l in reversed(lines):
        if re.match(r"^\w*(Error|Exception|Warning)\b", l):
            return l
    return ""


def classify_error(text):
    """Return (category, fixable, hint) for an error string."""
    t = (text or "")
    tail = t[-2000:] if len(t) > 2000 else t
    # Infra (non-fixable) patterns get first say, judged on the final
    # exception line — tracebacks put the real cause last, so a "429" or
    # "TimeoutError" buried under a traceback header must not classify as
    # a fixable solver_crash.
    final = _final_exception_line(tail)
    for rx, cat, fixable, hint in PATTERNS:
        if not fixable and re.search(rx, final or tail, re.IGNORECASE):
            return cat, fixable, hint
    # Then every pattern, judged on the tail (which holds the traceback
    # header for genuine code crashes).
    for rx, cat, fixable, hint in PATTERNS:
        if re.search(rx, tail, re.IGNORECASE):
            return cat, fixable, hint
    return "unknown", False, "Unrecognized failure shape; route around it."


def _write_journal(episode):
    os.makedirs(os.path.dirname(DEBUG_JOURNAL), exist_ok=True)
    with open(DEBUG_JOURNAL, "a") as f:
        f.write(f"\n## {episode['ts'][:19]}Z gen{episode['gen']}/p{episode['proposal_idx']} "
                f"— {episode['category']} — "
                f"{'FIXED' if episode['fixed'] else 'not fixed'}\n")
        f.write(f"Error: {episode['error_excerpt']}\n\n")
        f.write(f"Fix attempted: {episode['fix_attempted']}\n")
        if episode.get("fix_summary"):
            f.write(f"Fix: {episode['fix_summary']}\n")


def record_episode(gen, proposal_idx, category, error_text, fix_attempted,
                   fixed, fix_summary="", proposed=False):
    """Journal the episode and teach the notebook. Returns the episode dict.

    FIX #2 (Opus review 2026-10-09): a repair is PROPOSED when the coder
    produces a diff, VERIFIED only after the caller re-grades it. Lessons
    ("try that repair first") are earned by passing re-grade — recording
    them at proposal time taught the notebook fixes that never worked.
    Proposed episodes are journaled but write no lesson; the caller closes
    the loop with record_verification().
    """
    episode = {
        "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "gen": gen,
        "proposal_idx": proposal_idx,
        "category": category,
        "error_excerpt": (error_text or "")[:300].replace("\n", " "),
        "fix_attempted": fix_attempted,
        "fixed": fixed,
        "proposed": proposed,
        "fix_summary": fix_summary[:300],
    }
    try:
        _write_journal(episode)
    except Exception:
        pass
    if proposed:
        # No lesson yet — the repair hasn't earned one.
        return episode
    # The lesson the collective keeps: what this error was, and whether
    # the automatic fix worked.
    try:
        if fixed:
            lesson = (f"Auto-debug FIXED a '{category}' failure: {fix_summary[:160]} "
                      f"When this error appears, try that repair first.")
            reason = f"auto-debug repaired: {category}"
        elif fix_attempted:
            lesson = (f"Auto-debug tried and FAILED on '{category}': {fix_summary[:160]} "
                      f"Do not burn more calls retrying this shape of failure.")
            reason = f"auto-debug failed: {category}"
        else:
            lesson = (f"'{category}' is not auto-fixable ({fix_summary[:160]}). "
                      f"Route around it instead of retrying.")
            reason = f"auto-debug skipped: {category}"
        finding = {
            "ts": episode["ts"],
            "gen": gen,
            "proposal_idx": proposal_idx,
            "tried": f"auto-debug on {category}: {episode['error_excerpt'][:110]}",
            "outcome": "auto-debug fixed" if fixed else "auto-debug failed",
            "reason": reason,
            "score_before": None,
            "score_after": None,
            "lesson": lesson,
        }
        os.makedirs(os.path.dirname(FINDINGS_PATH), exist_ok=True)
        with open(FINDINGS_PATH, "a") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            try:
                f.write(json.dumps(finding) + "\n")
            finally:
                fcntl.flock(f, fcntl.LOCK_UN)
    except Exception:
        pass
    return episode


def record_verification(episode, verified, note=""):
    """Close the loop on a PROPOSED repair: the caller re-graded it.

    Writes the notebook lesson only now. A proposed fix that still crashes
    teaches "failed, don't retry this shape" instead of "FIXED".
    Returns the updated episode dict.
    """
    episode["fixed"] = bool(verified)
    episode["proposed"] = False
    episode["verification_note"] = (note or "")[:200]
    try:
        _write_journal(episode)
    except Exception:
        pass
    # Reuse the lesson writer by re-recording as a closed episode.
    record_episode(episode["gen"], episode["proposal_idx"],
                   episode["category"], episode["error_excerpt"],
                   True, bool(verified),
                   (note or episode["fix_summary"])[:300])
    return episode


def _coder_repair(coder_prompt, coder_call, task_desc, broken_artifact,
                  error_text, hint):
    """One bounded coder call to repair a broken artifact. Returns text."""
    prompt = (f"{coder_prompt}\n\n"
              f"AUTO-DEBUG: the artifact below {task_desc}.\n"
              f"Hint: {hint}\n\n"
              f"Error:\n{error_text[:1500]}\n\n"
              f"Broken artifact:\n{broken_artifact[:6000]}\n\n"
              f"Output ONLY a corrected unified diff (git-style, a/ b/ "
              f"prefixes) that repairs it. If it cannot be repaired, output "
              f"exactly: UNFIXABLE")
    try:
        out = coder_call(prompt)
    except Exception as e:
        return None, f"repair call raised {e}"[:120]
    if not out or out.startswith("ERROR:") or "UNFIXABLE" in out[:60]:
        return None, "coder declined or the call failed"
    return out, ""


def attempt_diff_repair(diff_text, patch_error, pristine_dir, coder_prompt,
                       coder_call, gen=0, proposal_idx=0):
    """Try once to repair a diff that failed to apply.

    Returns (fixed_diff_or_None, episode). The fixed diff is verified to
    pass the allowlist gate and apply cleanly on a fresh copy.
    """
    from controller import apply_diff, diff_touches_forbidden
    category, fixable, hint = classify_error(patch_error)
    if not fixable:
        return None, record_episode(
            gen, proposal_idx, category, patch_error, False, False, hint)
    fixed, why = _coder_repair(coder_prompt, coder_call,
                               "failed to apply as a patch",
                               diff_text, patch_error, hint)
    if fixed is None:
        return None, record_episode(
            gen, proposal_idx, category, patch_error, True, False, why)
    forbidden, bad = diff_touches_forbidden(fixed)
    if forbidden:
        return None, record_episode(
            gen, proposal_idx, category, patch_error, True, False,
            f"repaired diff touched forbidden path {bad}; discarded")
    probe = tempfile.mkdtemp(prefix="autodebug_probe_")
    try:
        shutil.copytree(pristine_dir, probe, dirs_exist_ok=True)
        ok, err = apply_diff(probe, fixed)
    finally:
        shutil.rmtree(probe, ignore_errors=True)
    if not ok:
        return None, record_episode(
            gen, proposal_idx, category, patch_error, True, False,
            f"repaired diff still did not apply: {err[:120]}")
    return fixed, record_episode(
        gen, proposal_idx, category, patch_error, True, True,
        "coder regenerated the diff; it applies cleanly")


def attempt_solver_repair(crashed_solver_path, error_text, coder_prompt,
                          coder_call, gen=0, proposal_idx=0):
    """Try once to repair a solver that crashed during grading.

    Returns (fix_diff_or_None, episode). The diff is against the crashed
    solver's current content; the caller applies and re-grades.
    """
    category, fixable, hint = classify_error(error_text)
    # Only solver-shaped crashes are repairable; infra flakes are not.
    if category not in ("solver_syntax", "solver_crash"):
        return None, record_episode(
            gen, proposal_idx, category, error_text, False, False, hint)
    try:
        with open(crashed_solver_path) as f:
            code = f.read()
    except OSError:
        return None, record_episode(
            gen, proposal_idx, category, error_text, True, False,
            "could not read the crashed solver")
    fixed, why = _coder_repair(coder_prompt, coder_call,
                               "crashed during grading", code,
                               error_text, hint)
    if fixed is None:
        return None, record_episode(
            gen, proposal_idx, category, error_text, True, False, why)
    from controller import diff_touches_forbidden
    forbidden, bad = diff_touches_forbidden(fixed)
    if forbidden:
        return None, record_episode(
            gen, proposal_idx, category, error_text, True, False,
            f"repair diff touched forbidden path {bad}; discarded")
    # Probe-apply on a pristine copy of the crashed solver: a diff that
    # does not even apply is not a repair (same discipline as
    # attempt_diff_repair).
    from controller import apply_diff as _apply
    probe = tempfile.mkdtemp(prefix="autodebug_sprobe_")
    try:
        shutil.copy(crashed_solver_path, os.path.join(probe, "solver.py"))
        ok, err = _apply(probe, fixed)
    finally:
        shutil.rmtree(probe, ignore_errors=True)
    if not ok:
        return None, record_episode(
            gen, proposal_idx, category, error_text, True, False,
            f"repair diff did not apply: {err[:120]}")
    # PROPOSED, not fixed: the caller re-grades and closes the loop with
    # record_verification(). No lesson is written until then.
    return fixed, record_episode(
        gen, proposal_idx, category, error_text, True, False,
        "coder produced a repair diff; proposed, awaiting re-grade",
        proposed=True)
