"""Stub solver for integration testing: returns reference solutions.

Usage: python3 harness/grade.py --solver harness/stub_solver.py --tasks dev
Expected: 100% pass. Any failure means the grader/sandbox wiring is broken,
not the solver.
"""
import json
import os

_BASE = os.path.dirname(os.path.abspath(__file__))
_SOLUTIONS = json.load(open(os.path.join(_BASE, "solutions.json")))


def solve(task):
    return _SOLUTIONS[task["id"]]["reference"]
