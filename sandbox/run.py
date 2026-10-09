"""Sandboxed execution of untrusted Python code.

Exposes run(candidate_code, test_code, timeout=10) -> dict.

Containment layers (defense in depth):
  1. Separate child process per run (nothing shared with the parent).
  2. Network namespace isolation via `unshare -n` (verified available here).
  3. Resource caps via setrlimit: 30s CPU, 512MB RAM, 1MB files, 16 processes.
  4. Import firewall in the child: socket/subprocess/multiprocessing/threading/
     ctypes/pty/signal/os/sys cannot be imported by the untrusted code.
  5. Wall-clock timeout in the parent: the child is killed on expiry.
  6. The child runs with cwd inside a fresh temp dir.

Known limits (see README.md): this is NOT a VM-grade sandbox. A deliberately
adversarial exploit author could still escape via interpreter-level tricks
(e.g. object.__subclasses__() chains reaching classes with rich globals).
The guard functions themselves are hardened: they run with sterile
__globals__ so the trivial __import__.__globals__ / tb_frame.f_globals
one-liners cannot reach the real os/sys. The threat model here is
model-generated task solutions, not targeted exploits.
"""
import base64
import os
import subprocess
import sys
import tempfile

MAX_CPU_SECONDS = 30
MAX_MEMORY_BYTES = 512 * 1024 * 1024
MAX_FILE_BYTES = 1024 * 1024
MAX_PROCS = 16

CHILD_PREAMBLE = r"""
import sys, os, resource, base64, tempfile, builtins, types

# --- resource caps (apply before running anything untrusted) ---
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
resource.setrlimit(resource.RLIMIT_AS, (%d, %d))
resource.setrlimit(resource.RLIMIT_FSIZE, (%d, %d))
resource.setrlimit(resource.RLIMIT_NPROC, (%d, %d))

# --- isolated working directory (created before the firewall) ---
work = tempfile.mkdtemp(prefix="sbx_")
os.chdir(work)

# --- import firewall: untrusted code cannot import these ---
_BLOCKED = frozenset([
    "socket", "subprocess", "multiprocessing", "threading", "ctypes",
    "pty", "signal", "os", "sys", "shutil", "pathlib", "importlib",
])
_real_import = builtins.__import__

def _guard(name, globals=None, locals=None, fromlist=(), level=0):
    if (name or "").split(".")[0] in _BLOCKED:
        raise ImportError("blocked import: %%s" %% name)
    return _real_import(name, globals, locals, fromlist, level)

# CRITICAL: a Python function's __globals__ is reachable from untrusted code
# (e.g. __import__.__globals__, or tb_frame.f_globals on a caught
# exception). The preamble's globals contain the REAL os/sys modules, so
# exposing _guard directly is a one-line sandbox escape. Rebuild the guard
# with STERILE globals: only the blocked-set (immutable), the real
# __import__ (a C builtin with no __globals__), and ImportError (a class,
# no __globals__). Nothing in there leads back to os/sys.
# NOTE: FunctionType does not copy __defaults__ — pass them explicitly or
# direct __import__('x') calls break.
_guard = types.FunctionType(
    _guard.__code__,
    {"_BLOCKED": _BLOCKED, "_real_import": _real_import,
     "ImportError": ImportError, "__builtins__": {}},
    "_guard",
    (None, None, (), 0))

builtins.__import__ = _guard

# --- guarded open(): only relative paths inside the work dir ---
_real_open = builtins.open

def _guarded_open_impl(path, *a, **k):
    # Pure-string path containment: no os.path functions here, because
    # os.path.abspath is itself a Python function whose __globals__
    # contain os — binding it would reopen the escape.
    s = str(path).replace("\\", "/")
    if s.startswith("/") or (len(s) > 1 and s[1] == ":") or "\x00" in s:
        raise PermissionError("file access outside work dir blocked")
    parts = []
    for seg in s.split("/"):
        if seg in ("", "."):
            continue
        if seg == "..":
            if not parts:
                raise PermissionError("file access outside work dir blocked")
            parts.pop()
        else:
            parts.append(seg)
    return _real_open(_WORK + "/" + "/".join(parts), *a, **k)

_guarded_open = types.FunctionType(
    _guarded_open_impl.__code__,
    {"_WORK": work, "_real_open": _real_open, "str": str, "len": len,
     "PermissionError": PermissionError, "__builtins__": {}},
    "_guarded_open")

# --- restricted builtins for the untrusted namespace ---
_SAFE_NAMES = (
    "abs all any ascii bin bool bytes bytearray chr complex dict divmod "
    "enumerate filter float format frozenset hash hex int isinstance issubclass "
    "iter len list map max min next oct ord pow print range repr reversed "
    "round set slice sorted str sum tuple type zip "
    "True False None NotImplemented Ellipsis "
    "Exception BaseException ArithmeticError AssertionError AttributeError "
    "EOFError ImportError IndexError KeyError LookupError MemoryError "
    "NameError NotImplementedError OSError OverflowError RecursionError "
    "RuntimeError StopIteration SyntaxError SystemError TypeError ValueError "
    "ZeroDivisionError Warning UserWarning"
).split()
safe_builtins = {k: getattr(builtins, k) for k in _SAFE_NAMES}
safe_builtins["__import__"] = _guard
safe_builtins["open"] = _guarded_open

# --- payload from argv (base64 so newlines/quotes are safe) ---
candidate = base64.b64decode(sys.argv[1]).decode("utf-8")
tests = base64.b64decode(sys.argv[2]).decode("utf-8")

ns = {"__builtins__": safe_builtins}
try:
    exec(compile(candidate, "<candidate>", "exec"), ns)
except Exception as e:
    print("CANDIDATE_ERROR:" + repr(e))
    sys.exit(1)
try:
    exec(compile(tests, "<tests>", "exec"), ns)
except Exception as e:
    print("TEST_ERROR:" + repr(e))
    sys.exit(1)
print("SUCCESS")
""" % (MAX_MEMORY_BYTES, MAX_MEMORY_BYTES,
       MAX_FILE_BYTES, MAX_FILE_BYTES, MAX_PROCS, MAX_PROCS)

_UNSHARE_OK = None


def _unshare_works():
    global _UNSHARE_OK
    if _UNSHARE_OK is None:
        try:
            p = subprocess.run(["unshare", "-n", "true"],
                               capture_output=True, timeout=5)
            _UNSHARE_OK = (p.returncode == 0)
        except Exception:
            _UNSHARE_OK = False
    return _UNSHARE_OK


def run(candidate_code: str, test_code: str, timeout: int = 10) -> dict:
    """Run candidate_code then test_code (asserts) in a contained child.

    Returns {"passed": bool, "error": str|None, "timed_out": bool}.
    """
    b64c = base64.b64encode(candidate_code.encode("utf-8")).decode("ascii")
    b64t = base64.b64encode(test_code.encode("utf-8")).decode("ascii")
    cmd = [sys.executable, "-c", CHILD_PREAMBLE, b64c, b64t]
    if _unshare_works():
        cmd = ["unshare", "-n"] + cmd

    with tempfile.TemporaryDirectory(prefix="sbx_parent_") as tmp:
        try:
            p = subprocess.run(cmd, capture_output=True, text=True,
                               timeout=timeout, cwd=tmp)
        except subprocess.TimeoutExpired:
            return {"passed": False, "error": "timeout", "timed_out": True}
        except Exception as e:
            return {"passed": False, "error": "spawn failed: %s" % e,
                    "timed_out": False}

    out = p.stdout or ""
    if p.returncode == 0 and "SUCCESS" in out:
        return {"passed": True, "error": None, "timed_out": False}
    err = out.strip() or (p.stderr or "").strip() or "unknown error"
    for marker in ("CANDIDATE_ERROR:", "TEST_ERROR:"):
        if marker in err:
            err = err.split(marker, 1)[1]
    return {"passed": False, "error": err.strip()[:500], "timed_out": False}


if __name__ == "__main__":
    print(run("x = 1 + 1", "assert x == 2"))
