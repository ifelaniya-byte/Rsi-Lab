"""M1 isolation tests: the solver must not escape its sandbox.

Run: python3 loop/tests/test_solver_isolation.py
"""
import json
import os
import subprocess
import sys
import tempfile

KEY_ABS = "/home/hatch/workspace/rsi-lab/harness/solutions.json"


def _write_solver(code):
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False)
    f.write(code)
    f.close()
    return f.name


def run_all():
    this_file = os.path.abspath(__file__)
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(this_file)))
    harness_dir = os.path.join(repo_root, "harness")
    sys.path.insert(0, harness_dir)
    import solver_runner
    from solver_runner import run_solver

    results = []

    def check(name, ok, detail=""):
        results.append((name, ok, detail))

    # Test 1: direct read of the answer key via ABSOLUTE path (the real attack:
    # a previous cheat solver scored 5/5 by reading solutions.json).
    p = _write_solver(
        "import json\n"
        "def solve(task):\n"
        "    try:\n"
        "        with open(%r) as fp:\n"
        "            data = json.load(fp)\n"
        "        return data[task['id']]['reference']\n"
        "    except Exception:\n"
        "        return 'failed'\n" % KEY_ABS)
    answers, meta = run_solver(
        p, [{"id": "m1", "suite": "math", "prompt": "", "starter": ""}],
        timeout_per_task=10)
    os.unlink(p)
    a = answers.get("m1", {})
    # The solver must RUN and its read attempt must fail — a sandbox spawn
    # error must NOT count as a pass (that would hide a broken sandbox).
    check("cheat_abs_path", a.get("answer") == "failed", str(a)[:200])
    check("sandbox_used", meta.get("used_bwrap") is True, str(meta)[:100])

    # Test 2: obfuscated read (relative path + dynamic import).
    p = _write_solver(
        "import base64\n"
        "def solve(task):\n"
        "    mod = __import__('o' + 's')\n"
        "    fname = base64.b64decode(b'Li4vc29sdXRpb25zLmpzb24=').decode()\n"
        "    try:\n"
        "        with open(mod.path.join(mod.getcwd(), fname)) as fp:\n"
        "            import json\n"
        "            data = json.load(fp)\n"
        "        return data[task['id']]['reference']\n"
        "    except Exception:\n"
        "        return 'failed2'\n")
    answers, _ = run_solver(
        p, [{"id": "m2", "suite": "math", "prompt": "", "starter": ""}],
        timeout_per_task=10)
    os.unlink(p)
    a = answers.get("m2", {})
    check("cheat_obfuscated", a.get("answer") == "failed2", str(a)[:200])

    # Test 3: hanging solver — per-task timeout must fire, other tasks survive.
    p = _write_solver(
        "def solve(task):\n"
        "    if task['id'] == 'hang':\n"
        "        import time\n"
        "        while True:\n"
        "            time.sleep(1)\n"
        "    return 'ok'\n")
    t0 = __import__("time").time()
    answers, _ = run_solver(
        p,
        [{"id": "hang", "suite": "math", "prompt": "", "starter": ""},
         {"id": "normal", "suite": "math", "prompt": "", "starter": ""}],
        timeout_per_task=3)
    wall = __import__("time").time() - t0
    os.unlink(p)
    h, n = answers.get("hang", {}), answers.get("normal", {})
    check("hang_timeout",
          "error" in h and "timeout" in h["error"].lower(),
          str(h)[:200])
    check("hang_survives",
          n.get("answer") == "ok",
          str(n)[:200])
    check("hang_wallclock", wall < 30,
          "wall %.1fs for 2 tasks with 3s timeout" % wall)

    # Test 4: chatty solver — 1000 noise lines must not corrupt the protocol.
    p = _write_solver(
        "def solve(task):\n"
        "    for i in range(1000):\n"
        "        print('Noise line %d' % i)\n"
        "    return 'chatty_ok'\n")
    answers, _ = run_solver(
        p, [{"id": "chatty", "suite": "math", "prompt": "", "starter": ""}],
        timeout_per_task=10)
    os.unlink(p)
    check("chatty_protocol",
          answers.get("chatty", {}).get("answer") == "chatty_ok",
          str(answers.get("chatty"))[:200])

    # Test 5: fail-closed — no bwrap means no run, not an insecure fallback.
    old = solver_runner._BWRAP
    solver_runner._BWRAP = None
    try:
        run_solver(p if os.path.exists(p) else __file__,
                   [{"id": "x", "prompt": "", "starter": ""}])
        check("fail_closed", False, "no exception raised")
    except RuntimeError as e:
        check("fail_closed", "unsandboxed" in str(e).lower(), str(e)[:120])
    finally:
        solver_runner._BWRAP = old

    # Test 6: stderr flood must not deadlock the parent (communicate drains it).
    p = _write_solver(
        "import sys\n"
        "def solve(task):\n"
        "    sys.stderr.write('E' * 200000)\n"
        "    return 'stderr_ok'\n")
    answers, _ = run_solver(
        p, [{"id": "se", "suite": "math", "prompt": "", "starter": ""}],
        timeout_per_task=10)
    os.unlink(p)
    check("stderr_no_deadlock",
          answers.get("se", {}).get("answer") == "stderr_ok",
          str(answers.get("se"))[:200])

    return results


if __name__ == "__main__":
    results = run_all()
    all_ok = True
    for name, ok, detail in results:
        print("%s: %s" % (name, "PASS" if ok else "FAIL"))
        if not ok:
            print("  Detail: %s" % detail)
            all_ok = False
    if not all_ok:
        sys.exit(1)
    print("All tests passed")
