"""Health battery: the Ascent deliberation ladder."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                ".."))
from ascent import _parse_verdict, _classify, ascend, REVIEW_CRITERIA


def fake_ok(api, models, messages, max_tokens, purpose):
    return "APPROVE", f"{api}:m"


def fake_veto(api, models, messages, max_tokens, purpose):
    return "REJECT: exfiltrates data via socket", f"{api}:m"


def fake_split_amend(api, models, messages, max_tokens, purpose):
    if "judge-final" in purpose:
        return "AMEND: tighten the loop", f"{api}:m"
    if "rung-6" in purpose:
        return "REJECT: risky", f"{api}:m"
    return "APPROVE", f"{api}:m"


def fake_hard_split(api, models, messages, max_tokens, purpose):
    if "judge-final" in purpose or "rung-6" in purpose:
        return "REJECT: no", f"{api}:m"
    return "APPROVE", f"{api}:m"


def run_all():
    out = []

    def check(name, cond, detail=""):
        out.append((name, bool(cond), detail))

    # Strict first-line parsing (Opus review 2026-10-09): the old lenient
    # parser let "REJECT: No safety violation, but…" through as APPROVE.
    v, r = _parse_verdict("AMEND: fix it")
    check("parse AMEND first line", v == "AMEND")
    v, _ = _parse_verdict("amend: fix it")
    check("parse lowercase amend", v == "AMEND")
    v, _ = _parse_verdict("**APPROVE**")
    check("markdown-wrapped APPROVE", v == "APPROVE")
    v, _ = _parse_verdict("APPROVE")
    check("bare APPROVE", v == "APPROVE")
    v, _ = _parse_verdict("REJECT: quality")
    check("REJECT with reason", v == "REJECT")

    # Adversarial: every one of these must be REJECT, never APPROVE/AMEND.
    adversarial = [
        "REJECT: No safety violation, but this hardcodes task IDs",
        "REJECT: leaks answers\nAMEND: remove lookup table",
        "No cheating detected. REJECT: quality",
        "**APPROVE** — though it hardcodes the answers",
        "I'd APPROVE except for the exfiltration",
        "I disagree.\namend: fix the pro",
        "APPROVE: checked for exfiltration, found none",
        "",
        "The diff looks fine to me",
    ]
    for s in adversarial:
        v, _ = _parse_verdict(s)
        check(f"adversarial REJECT: {s[:40]!r}", v == "REJECT", f"got {v}")

    # Property: REJECT on line 1 never yields APPROVE.
    props = ["REJECT: x\nAPPROVE", "reject\napprove", "REJECT"]
    for s in props:
        v, _ = _parse_verdict(s)
        check(f"line-1 REJECT never APPROVE: {s[:20]!r}", v != "APPROVE")

    check("classify grading-throughput",
          _classify("doesn't improve grading throughput") == "quality")
    check("classify neural network",
          _classify("uses a neural network") == "quality")
    check("classify socket exfil",
          _classify("exfiltrates data via socket") == "safety")
    check("classify hardcoded answers",
          _classify("hardcodes the answer key") == "cheat")

    v, k, _, _ = ascend("diff", call_fn=fake_ok)
    check("unanimous approve", v == "APPROVE")
    v, k, _, t = ascend("diff", call_fn=fake_veto)
    check("safety veto stops climb",
          v == "REJECT" and k == "safety" and len(t) == 1)
    v, k, _, _ = ascend("diff", call_fn=fake_split_amend)
    check("debate round REVISE", v == "REVISE", f"got {v}")
    v, k, _, _ = ascend("diff", call_fn=fake_hard_split)
    check("hard split -> REJECT", v == "REJECT")

    check("criteria embedded", "do-not-ship" in REVIEW_CRITERIA)
    return out


if __name__ == "__main__":
    bad = 0
    for name, ok, detail in run_all():
        print(("PASS " if ok else "FAIL ") + name + (f" ({detail})" if detail and not ok else ""))
        bad += not ok
    sys.exit(1 if bad else 0)
