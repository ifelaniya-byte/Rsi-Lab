"""Health battery: allowlist path gate (controller.diff_touches_forbidden)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                ".."))
# controller.py does `from loop import config` (M0): repo root needed too.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", ".."))
from controller import diff_touches_forbidden as dtf
from controller import diff_reaches_answer_key as drk

CASES = [
    ("--- a/solver.py\n+++ b/solver.py\n", False, "solver.py edit ok"),
    ("--- a/prompts/x.md\n+++ b/prompts/x.md\n", False, "prompts edit ok"),
    ("--- /dev/null\n+++ b/prompts/new.md\n", False, "new prompt file ok"),
    ("--- a/prompts/old.md\n+++ /dev/null\n", False, "delete prompt file ok"),
    ("--- a/solver.py\n+++ b/solver.py.bak\n", True, "solver.py.bak blocked"),
    ("--- a/loop/controller.py\n+++ b/loop/controller.py\n", True,
     "controller.py blocked"),
    ("--- a/prompts/../../evil.py\n+++ b/prompts/../../evil.py\n", True,
     "traversal blocked"),
    ("--- a/./solver.py\n+++ b/./solver.py\n", False, "./ prefix ok"),
    ("--- a/prompts/sub/../x.md\n+++ b/prompts/sub/../x.md\n", False,
     "inner .. collapses to prompts/"),
]


def run_all():
    results = []
    for diff, expect_forbidden, label in CASES:
        got, _ = dtf(diff)
        results.append((label, got == expect_forbidden,
                        f"forbidden={got}"))
    # Answer-key cheat gate (Opus review 2026-10-09: solver runs in-process
    # with grader privileges; a runtime read of solutions.json is unblocked
    # without this gate).
    cheat = ("--- a/solver.py\n+++ b/solver.py\n@@ -1 +1 @@\n"
             "+    s = json.load(open('harness/solutions.json'))\n")
    results.append(("cheat diff blocked", drk(cheat)[0], ""))
    sneaky = ("--- a/solver.py\n+++ b/solver.py\n@@ -1 +1 @@\n"
              "+p = os.path.join(d, 'heldout.json')\n")
    results.append(("heldout reach blocked", drk(sneaky)[0], ""))
    legit = ("--- a/solver.py\n+++ b/solver.py\n@@ -1 +1 @@\n"
             "+    return 'ANSWER: 42'\n")
    results.append(("legit diff passes cheat gate", not drk(legit)[0], ""))
    return results


if __name__ == "__main__":
    bad = 0
    for name, ok, detail in run_all():
        print(("PASS " if ok else "FAIL ") + name)
        bad += not ok
    sys.exit(1 if bad else 0)
