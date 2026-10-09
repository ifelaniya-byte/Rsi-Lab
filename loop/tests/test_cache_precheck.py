#!/usr/bin/env python3
"""Drift tests for solver_runner's in-process cache pre-check.

The pre-check replicates solver.py's prompt construction, cache key, and
answer extraction. If solver.py drifts, the replica must DEGRADE (miss and
use the sandbox), never return a WRONG answer. These tests pin that:

1. precheck_hit_matches_sandbox: for cached tasks, the pre-check answer
   equals the sandbox's answer byte-for-byte.
2. precheck_miss_falls_back: a solver the cache has never seen gets zero
   pre-check hits and still grades via the sandbox.
3. replica_key_matches_solver: the replica key function produces the same
   key the solver itself would compute for a known task.
"""
import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE, "harness"))
sys.path.insert(0, os.path.join(BASE, "loop"))

from solver_runner import (_cache_lookup, _replica_prompt, _replica_cache_key,
                           _replica_extract, _run_one_task, run_solver)

SOLVER = os.path.join(BASE, "loop", "solver.py")
ENTRY = os.path.join(BASE, "harness", "solver_entry.py")
CACHE = os.path.join(BASE, "loop", ".solver_sandbox_cache",
                     ".solver_cache.jsonl")
TASKS = json.load(open(os.path.join(BASE, "harness", "tasks.json")))
DEV = [t for t in TASKS if t["dev"]][:4]


def test_precheck_hit_matches_sandbox():
    """Pre-check answer == sandbox answer for cached tasks."""
    assert os.path.exists(CACHE), "sandbox cache missing — run a grading first"
    for task in DEV:
        prompt, answer, usage = _cache_lookup(SOLVER, CACHE, task)
        if answer is None:
            print(f"  {task['id']}: no cache entry, skipping")
            continue
        # Force the sandbox path (its own cache check is the source of truth)
        result, _ = _run_one_task(SOLVER, ENTRY, CACHE, task, 60)
        assert "answer" in result, f"{task['id']}: sandbox errored: {result.get('error')}"
        assert result["answer"] == answer, (
            f"{task['id']}: DRIFT! pre-check={answer[:80]!r} "
            f"sandbox={result['answer'][:80]!r}")
        print(f"  {task['id']}: match ({len(answer)} chars)")
    print("PASS precheck_hit_matches_sandbox")


def test_precheck_miss_falls_back():
    """Unknown solver -> zero pre-check hits, sandbox still works."""
    import tempfile
    fake_solver = os.path.join(tempfile.mkdtemp(), "solver.py")
    open(fake_solver, "w").write("def solve(task):\n    return 'hi'\n")
    answers, meta = run_solver(fake_solver, DEV[:1], 30, workers=1)
    assert meta["cache_precheck_hits"] == 0, "unexpected pre-check hit"
    tid = DEV[0]["id"]
    assert answers[tid].get("answer") == "hi", answers[tid]
    print("PASS precheck_miss_falls_back")


def test_replica_key_matches_solver():
    """Replica key == solver's own key for a real task."""
    sys.path.insert(0, os.path.join(BASE, "loop"))
    import importlib.util
    spec = importlib.util.spec_from_file_location("solv", SOLVER)
    mod = importlib.util.module_from_spec(spec)
    # Don't exec the module (it has side effects at import); replicate the
    # key math directly from solver source instead.
    src = open(SOLVER).read()
    assert "_solver_cache_key" in src
    task = DEV[0]
    prompt = _replica_prompt(task)
    key = _replica_cache_key(SOLVER, task["id"], prompt)
    assert len(key) == 24 and all(c in "0123456789abcdef" for c in key)
    # And the key must actually find the cached entry (proves prompt replica
    # matches what the solver used when it wrote the cache).
    found = False
    with open(CACHE) as f:
        for line in f:
            try:
                r = json.loads(line)
            except Exception:
                continue
            if r.get("k") == key:
                found = True
                break
    assert found, "replica key found no cache entry — prompt replica drifted!"
    print("PASS replica_key_matches_solver")


if __name__ == "__main__":
    test_precheck_hit_matches_sandbox()
    test_precheck_miss_falls_back()
    test_replica_key_matches_solver()
    print("All drift tests passed")
