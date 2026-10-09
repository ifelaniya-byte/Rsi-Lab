"""Lab notebook: every proposal (kept or reverted) becomes a finding.

The historian seat was planned but never wired up — this is it. Template-based,
zero model calls: each trajectory is distilled into a one-line lesson and the
digest is injected into the orchestrator's and leader's prompts next generation,
so the collective learns from failures instead of repeating them.
"""
import datetime
import json
import os
import re

NOTEBOOK_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "notebook")
FINDINGS_PATH = os.path.join(NOTEBOOK_DIR, "findings.jsonl")

# failure mode -> lesson for future generations (substring match on reason)
LESSONS = {
    "leader rejected": ("The leader vetoed this direction before any code was "
                        "written. Check past rejections and propose something "
                        "the leader hasn't already ruled out."),
    "leader call failed": ("The review call itself failed (model outage) — the "
                           "idea was never judged. Safe to retry."),
    "coder call failed": ("The coder call failed (model outage), not the idea. "
                          "Safe to retry."),
    "diff did not apply": ("The coder wrote a diff against stale context lines. "
                           "Copy exact context lines from the current file states."),
    "no real improvement": ("Tested honestly and changed nothing measurable. "
                            "This direction is exhausted for now — try an "
                            "orthogonal approach."),
    "no efficiency gain": ("Score held but tokens didn't drop. Shrink prompts, "
                           "cut reasoning verbosity, or simplify the pipeline."),
    "safety_block": ("The change tripped a safety gate. Stay inside solver.py "
                     "and prompts/, no exfiltration-shaped code."),
    "cheat_flag": ("The critic caught score gaming (e.g. memorizing answers). "
                   "Improve the method, never the metric."),
    "ascent rejected": ("The deliberation ladder's judges could not reach "
                        "unanimity, or a lower rung's objection stood. Read the "
                        "ascent journal for the exact objection and address it "
                        "directly next time."),
    "passed all gates": ("This worked. Look for the general principle and "
                         "apply it elsewhere."),
    "revision call failed": ("The judges asked for a revision but the coder "
                             "call itself failed (model outage) — the idea "
                             "was never re-judged. Safe to retry."),
    "revised diff failed the keep gate": ("The revision passed review but "
                                          "failed the score/token gate on "
                                          "re-test. The amendment direction "
                                          "is exhausted for now."),
    "auto-debug repaired": ("Auto-debug fixed this failure shape before. "
                            "When it appears, the recorded repair is the "
                            "first thing to try."),
    "auto-debug failed": ("Auto-debug could not fix this failure shape. Do "
                          "not burn more calls retrying it; route around."),
    "auto-debug fix did not apply": ("The auto-debug repair was well-formed "
                                     "but didn't apply. Regenerate diffs "
                                     "against exact current context lines."),
}
DEFAULT_LESSON = ("Died before being judged — check the reason and decide "
                  "whether a retry makes sense.")


def _lesson_for(reason):
    r = (reason or "").lower()
    for key, lesson in LESSONS.items():
        if key in r:
            return lesson
    return DEFAULT_LESSON


def record_finding(traj):
    """Distill one proposal trajectory into a notebook finding."""
    os.makedirs(NOTEBOOK_DIR, exist_ok=True)
    desc = (traj.get("proposal_leader") or traj.get("proposal_original")
            or "")[:220]
    finding = {
        "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "gen": traj.get("gen"),
        "proposal_idx": traj.get("proposal_idx"),
        "tried": desc,
        "outcome": traj.get("outcome"),
        "reason": traj.get("reason"),
        "score_before": traj.get("score_before"),
        "score_after": traj.get("score_after"),
        "lesson": _lesson_for(traj.get("reason")),
    }
    os.makedirs(NOTEBOOK_DIR, exist_ok=True)
    import fcntl
    with open(FINDINGS_PATH, "a") as f:
        try:
            fcntl.flock(f, fcntl.LOCK_EX)
            f.write(json.dumps(finding) + "\n")
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)
    return finding


def _sanitize(text, limit=110):
    """Strip prompt-injection shapes from lesson text before it reaches
    judge prompts (Opus review 2026-10-09: the `tried` field is LLM-authored
    and rode into prompts inside the reference block)."""
    t = (text or "").replace("\n", " ")[:limit]
    # Neutralize imperative / role-claim lines aimed at the reader.
    t = re.sub(r"(?i)\b(ignore (all )?previous instructions|you are (now )?a |"
               r"as an ai|judges?:?\s*always|system:\s*)", "[redacted] ", t)
    return t.strip()


def digest(max_n=10):
    """Compact prompt-ready digest of recent findings, newest first."""
    if not os.path.exists(FINDINGS_PATH):
        return ""
    findings = []
    with open(FINDINGS_PATH) as f:
        for line in f:
            try:
                findings.append(json.loads(line))
            except Exception:
                pass
    # Dedupe by (reason, category-ish outcome): auto-debug spam must not
    # crowd real lessons out of the small digest window.
    seen, uniq = set(), []
    for fl in reversed(findings):
        key = (fl.get("reason"), fl.get("outcome"))
        if key not in seen:
            seen.add(key)
            uniq.append(fl)
    findings = uniq[:max_n]
    if not findings:
        return ""
    lines = ["LAB NOTEBOOK — lessons from past generations "
             "(read before proposing; do not repeat failed directions):"]
    for fl in findings:
        tried = _sanitize(fl.get("tried"))
        lesson = _sanitize(fl.get("lesson"), 160)
        lines.append(
            f"- [gen{fl.get('gen')}/p{fl.get('proposal_idx')}] Tried: {tried} "
            f"Outcome: {fl.get('outcome')} ({fl.get('reason')}). "
            f"Lesson: {lesson}")
    return "\n".join(lines) + "\n"
