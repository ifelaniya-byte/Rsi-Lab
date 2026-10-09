#!/usr/bin/env python3
"""Honest holdout evaluation (Codex recommendation #1).

Grades a solver on the 25 FROZEN holdout tasks only, with a Wilson
score confidence interval. The loop NEVER uses this for decisions —
it is the transfer check: does improvement on dev generalize?

Usage: python3 harness/eval_holdout.py --solver loop/solver.py [--timeout 10]
"""
import argparse
import contextlib
import importlib.util
import io
import json
import math
import os
import sys


def wilson(p, n, z=1.96):
    """Wilson score interval for a binomial proportion."""
    if n == 0:
        return (0.0, 0.0)
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (max(0.0, (c - m) / d), min(1.0, (c + m) / d))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solver", required=True)
    ap.add_argument("--timeout", type=int, default=10)
    args = ap.parse_args()

    base = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(base, "..", "sandbox"))
    from run import run

    tasks = json.load(open(os.path.join(base, "tasks.json")))
    solutions = json.load(open(os.path.join(base, "solutions.json")))
    holdout = set(json.load(open(os.path.join(base, "heldout.json")))["task_ids"])
    selected = [t for t in tasks if t["id"] in holdout]
    assert len(selected) == 25, f"holdout changed! got {len(selected)}"

    spec = importlib.util.spec_from_file_location("solver", args.solver)
    solver_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solver_module)

    per_suite = {}
    passed = 0
    for task in selected:
        sol = solutions[task["id"]]
        per_suite.setdefault(task["suite"], [0, 0])[0] += 1
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                code = solver_module.solve(task)
        except Exception:
            continue
        # Non-string output is a wrong answer, not a grader crash.
        if not isinstance(code, str):
            continue
        if task["suite"] == "math":
            ok = code.strip() == sol["reference"].strip()
        else:
            ok = run(code, sol["tests"], args.timeout)["passed"]
        if ok:
            passed += 1
            per_suite[task["suite"]][1] += 1

    n = len(selected)
    p = passed / n
    lo, hi = wilson(p, n)
    print(f"HOLDOUT: {passed}/{n} = {100*p:.1f}% "
          f"(95% CI: {100*lo:.1f}%–{100*hi:.1f}%)")
    for suite, (tot, ok) in sorted(per_suite.items()):
        print(f"  {suite}: {ok}/{tot} = {100*ok/tot:.1f}%")
    print("NOTE: for honest reporting only — never used for loop decisions.")


if __name__ == "__main__":
    main()
