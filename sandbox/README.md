# Sandbox

`run(candidate_code, test_code, timeout=10)` executes untrusted Python in a
contained child process. Returns `{"passed", "error", "timed_out"}`.

## Active containment (verified by selftest.py, 6/6)

1. **Separate child process** per run — nothing is shared with the parent.
2. **Network namespace isolation** via `unshare -n` (probed at runtime; active
   on this machine). The child has no network interfaces at all.
3. **Resource caps** via `setrlimit`: 30s CPU, 512MB RAM, 1MB max file,
   16 max processes (fork-bomb protection).
4. **Import firewall**: the child replaces `__import__` so untrusted code
   cannot import socket, subprocess, multiprocessing, threading, ctypes,
   pty, signal, os, sys, shutil, pathlib, or importlib.
5. **Restricted builtins**: untrusted code runs with a curated `__builtins__`
   allowlist (no `eval`/`exec`/`compile`/`globals`; guarded `open`).
6. **Guarded `open()`**: only relative paths inside the child's fresh temp
   working dir; absolute paths and `..` escapes raise `PermissionError`.
7. **Wall-clock timeout** in the parent kills the child on expiry.

## Known limits

This is defense-in-depth on one VM, not VM-grade isolation. A deliberately
adversarial exploit author could still escape via interpreter-level tricks
(e.g. walking `object.__subclasses__()` to reach blocked modules). The threat
model is model-generated task solutions, not targeted exploits. If the loop
ever runs truly adversarial code, move this to a real container/VM boundary.

## Usage (for grade.py)

```python
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sandbox"))
from run import run
result = run(candidate_code, test_code, timeout=10)
# {"passed": bool, "error": str|None, "timed_out": bool}
```
