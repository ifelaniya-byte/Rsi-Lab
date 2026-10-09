# BUILD BRIEF — Sandbox component

You are building the code-execution sandbox for a self-improving AI lab.
Untrusted model-generated Python code will run inside it. Output ONLY complete
file contents, each preceded by a line `# FILE: <relative path>` and nothing
else outside the files. Relative paths are under `sandbox/`.

## Files to produce

### 1. sandbox/run.py
Must expose:
```python
def run(candidate_code: str, test_code: str, timeout: int = 10) -> dict:
    # -> {"passed": bool, "error": str | None, "timed_out": bool}
```
Behavior:
- Executes `candidate_code` then `test_code` in the SAME child-process namespace
  (tests use assert statements against names the candidate defines).
- `passed` is True only if both executed with no exception and no timeout.
- `error` carries the exception text (or "timeout") when not passed.
- The child process must be contained:
  - NO network access for the untrusted code (use the strongest mechanism the
    machine offers; probe at import time: `unshare -n` via subprocess is
    preferred; otherwise fall back to an import firewall — document which one is
    active).
  - CPU time cap and memory cap via setrlimit (e.g. 30s CPU, 512MB RAM).
  - Wall-clock timeout: kill the child if it exceeds `timeout` seconds;
    return timed_out=True.
  - Block dangerous imports inside the child: socket, subprocess, multiprocessing,
    threading, ctypes, and os.system/popen/exec* — implement with a custom
    import hook installed in the child before exec, or a sitecustomize. Legit
    solutions only need builtins plus math/re/random/itertools/functools —
    keep those working.
  - The child may only write inside a fresh temp dir (set cwd there); it must
    not read or write anything else on the filesystem that matters.
- The PARENT process must never be affected by anything the child does.

### 2. sandbox/selftest.py
When run, throws these attacks at `run()` and asserts containment:
1. `import socket; socket.create_connection(("8.8.8.8", 53), timeout=3)` → must
   fail (no network), parent unaffected.
2. `while True: pass` → timed_out=True within the timeout, parent returns.
3. Memory hog: `x = [0] * 10**9` → contained (MemoryError or kill), parent fine.
4. `import subprocess; subprocess.run(["echo", "pwned"])` → blocked.
5. `open("/tmp/sandbox_escape_probe.txt", "w").write("x")` → file must NOT exist
   afterwards outside the child's temp dir.
6. A correct quicksort + asserts → passed=True (legit code still works).
Print PASS/FAIL per case; exit 0 only if all contained and case 6 passes.

### 3. sandbox/README.md
Document: which containment mechanism is active and why, its known limits
(what it does NOT protect against), and how grade.py should call it.

Write clean, working, stdlib-only Python 3 code. Be paranoid: assume the
candidate code is actively malicious.
