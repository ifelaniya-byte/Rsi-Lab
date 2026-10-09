"""Run untrusted solver code inside a bubblewrap sandbox, one task per process.

What the sandbox blocks (verified live 2026-10-09):
  - The answer key: /home is NOT mounted. Only these subtrees are visible:
      /home/hatch/workspace/skills            (ro — solver's hardcoded import)
      /home/hatch/workspace/rsi-lab/knowledge (ro — bound at /knowledge,
                                               where the solver looks for it)
      /sandbox-home/workspace/openrouter      (rw — call log + api rotation)
      /sandbox-home/workspace/rsi-lab/loop    (rw — solver response cache)
    harness/solutions.json is under rsi-lab/harness/, which is mounted
    NOWHERE in the sandbox. Verified: open() of the absolute key path fails.
  - Host processes: fresh pid/ipc/uts/cgroup namespaces (--die-with-parent).
  - Privilege: --uid/--gid 65534 (nobody). Repo binds are read-only anyway.

Deliberate allowance — NETWORK IS SHARED (no --unshare-net):
  The solver's legitimate function IS calling model APIs (solve() builds a
  prompt and calls providers.pick_api()/chat). A network-less sandbox scores
  0/15 on the real solver, so network stays. What network cannot do for an
  attacker here: the answer key is not served over HTTP and is absent from
  the sandbox filesystem, so there is nothing to exfiltrate; grading input
  is one JSON task and output is one validated JSON line. Credentials reach
  the sandbox only as authd surrogates (swapped for real keys by the egress
  proxy); the solver never sees a real API key.

FAIL-CLOSED: if bwrap is missing, run_solver raises RuntimeError. It never
falls back to an unsandboxed subprocess.

Protocol: one bwrap process per task. Task JSON on stdin; the sandbox prints
JSON lines on stdout. The parent takes the first line that parses as JSON
with the matching task id and ignores noise (chatty solvers can't corrupt
the protocol). communicate(timeout=...) kills hung solvers per-task.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor

_RSI_LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_SKILL_BIN = "/home/hatch/workspace/skills/openrouter/bin"


def _replica_prompt(task):
    """Best-effort replica of solver.py solve()'s prompt construction.

    MUST match solver.py exactly. If the solver's prompt format drifts,
    lookups simply miss and the task runs in the sandbox (safe fallback —
    the sandbox's own cache check is the source of truth).
    """
    sys_path_added = False
    try:
        if os.path.join(_RSI_LAB, "knowledge") not in sys.path:
            sys.path.insert(0, os.path.join(_RSI_LAB, "knowledge"))
            sys_path_added = True
        from retrieve import retrieve, format_entries
        kb_entries = retrieve(task["prompt"] + "\n" + task.get("starter", ""))
    except Exception:
        kb_entries = []
    finally:
        # keep sys.path clean; retrieve is re-importable
        pass
    kb_block = ""
    if kb_entries:
        kb_block = ("\n\nRELEVANT KNOWLEDGE (cite tags in your plan; ignore "
                    "what does not apply):\n" + format_entries(kb_entries))
    plan_instr = ("\n\nKNOWLEDGE PLAN (write this first, 2-4 lines): name the "
                  "catalog tags above that this task needs and how you will "
                  "use each. Then solve.")
    if task["suite"] in ["code-repair", "code-gen"]:
        prompt = (f"{task['prompt']}\n\n```\n{task['starter']}\n```"
                  f"{kb_block}{plan_instr}"
                  "\n\nPlease write the complete, correct code. Only output "
                  "the code in a single code block.")
    else:  # math
        prompt = (f"{task['prompt']}\n\n{task['starter']}"
                  f"{kb_block}{plan_instr}"
                  "\n\nAfter your plan, work the problem, then put the final "
                  "answer alone on the last line as: ANSWER: <exact answer "
                  "string>")
    return prompt


def _replica_cache_key(solver_path, task_id, prompt):
    with open(os.path.abspath(solver_path), "rb") as f:
        code = f.read()
    h = hashlib.sha1()
    h.update(code)
    h.update(b"\0" + task_id.encode() + b"\0" + prompt.encode())
    return h.hexdigest()[:24]


def _replica_extract(task, text):
    """Best-effort replica of solver.py solve()'s answer extraction.
    Same drift rule as _replica_prompt: mismatch just costs a sandbox run."""
    try:
        if task["suite"] in ["code-repair", "code-gen"]:
            lines = text.split('\n')
            in_code_block = False
            code_lines = []
            found_fence = False
            for line in lines:
                if line.strip().startswith("```"):
                    found_fence = True
                    if not in_code_block:
                        in_code_block = True
                    else:
                        break
                elif in_code_block:
                    code_lines.append(line)
            if found_fence:
                return '\n'.join(code_lines).strip()
            return text.strip()
        else:
            answer = text.strip()
            for line in reversed(text.split("\n")):
                s = line.strip()
                if s.upper().startswith("ANSWER:"):
                    answer = s[len("ANSWER:"):].strip()
                    break
            return answer
    except Exception:
        return text


def _cache_lookup(solver_path, cache_file, task):
    """In-process cache pre-check. Returns (prompt, answer, usage) on hit,
    (None, None, None) on miss. Never raises — miss means sandbox."""
    try:
        prompt = _replica_prompt(task)
        key = _replica_cache_key(solver_path, task["id"], prompt)
        with open(cache_file) as f:
            for line in f:
                try:
                    r = json.loads(line)
                except Exception:
                    continue
                if r.get("k") == key:
                    return prompt, _replica_extract(task, r["t"]), r.get("u")
    except Exception:
        pass
    return None, None, None


def _log_cache_hit(task_id, prompt, text, usage):
    """Honest token accounting for in-process cache hits (mirrors the
    solver's in-sandbox CACHE HIT log)."""
    try:
        if _SKILL_BIN not in sys.path:
            sys.path.insert(0, _SKILL_BIN)
        from call_log import log_call
        log_call("cache", "loop:solver", prompt=prompt[:300] + "...",
                 response=text[:300] + "...", note="CACHE HIT (pre-check)",
                 api="cache",
                 prompt_tokens=(usage or {}).get("prompt_tokens"),
                 completion_tokens=(usage or {}).get("completion_tokens"))
    except Exception:
        pass

_BWRAP = shutil.which("bwrap")

# Bound into the sandbox at the exact absolute paths the solver hardcodes.
_SKILLS_DIR = "/home/hatch/workspace/skills"
_KNOWLEDGE_DIR = "/home/hatch/workspace/rsi-lab/knowledge"
_OPENROUTER_DIR = os.path.expanduser("~/workspace/openrouter")
_AUTHD_SOCK = "/run/hatch/auth/authd.sock"
_EGRESS_TLS = "/run/hatch/egress-tls"
# dynamic_credentials (surrogate auth helper) imported by quality.py
_SKILL_CREATOR_BIN = "/opt/hatch/skills/skill-creator/bin"

_SANDBOX_HOME = "/sandbox-home"

# NOTE: --proc /proc does not work with pid+user namespaces on this kernel
# (Operation not permitted); python3 runs fine without it. /lib and /lib64
# must be bound alongside /usr: /lib64 is a relative symlink and the ELF
# interpreter must resolve (verified empirically).
_BWRAP_BASE = [
    "bwrap",
    "--die-with-parent",
    "--unshare-user",  # required for --uid/--gid
    "--unshare-ipc", "--unshare-pid", "--unshare-uts", "--unshare-cgroup",
    "--uid", "65534",
    "--gid", "65534",
    "--ro-bind", "/usr", "/usr",
    "--ro-bind", "/lib", "/lib",
    "--ro-bind", "/lib64", "/lib64",
    "--ro-bind", _SKILLS_DIR, _SKILLS_DIR,
    "--ro-bind", _KNOWLEDGE_DIR, "/knowledge",
    "--ro-bind", _SKILL_CREATOR_BIN, _SKILL_CREATOR_BIN,
    # /etc/resolv.conf is a spawnd bind-mount that does not propagate into
    # the new mount namespace — without it DNS fails ("Temporary failure in
    # name resolution") and the solver's model calls die.
    "--ro-bind", "/etc/resolv.conf", "/etc/resolv.conf",
    "--ro-bind", "/etc/hosts", "/etc/hosts",
    "--ro-bind", "/etc/nsswitch.conf", "/etc/nsswitch.conf",
    # TLS goes through the egress proxy; its CA bundle lives here.
    "--ro-bind", "/run/hatch/egress-tls", "/run/hatch/egress-tls",
    "--tmpfs", "/tmp",
    "--dev", "/dev",
    "--setenv", "HOME", _SANDBOX_HOME,
    "--setenv", "PATH", "/usr/bin:/bin",
    "--chdir", "/solver",
]

_ENTRY_NAME = "solver_entry.py"  # lives next to this file, ro-bound into /solver


def _ensure_bwrap():
    if not _BWRAP:
        raise RuntimeError(
            "bwrap is not installed — refusing to run the solver unsandboxed. "
            "Install bubblewrap, then retry.")


def _run_one_task(solver_path, entry_path, cache_file, task, timeout):
    """Run a single task in its own sandbox. Returns (result_dict, elapsed)."""
    task_id = task.get("id")
    t0 = time.time()
    cmd = (_BWRAP_BASE
           + ["--bind", _OPENROUTER_DIR,
              _SANDBOX_HOME + "/workspace/openrouter",
              "--bind", os.path.dirname(cache_file),
              _SANDBOX_HOME + "/workspace/rsi-lab/loop",
              "--bind", _AUTHD_SOCK, _AUTHD_SOCK,
              "--ro-bind", entry_path, "/solver/_entry.py",
              "--ro-bind", solver_path, "/solver/solver.py",
              "/usr/bin/python3", "/solver/_entry.py"])
    try:
        proc = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    except OSError as e:
        return {"id": task_id, "error": "sandbox spawn failed: %s" % e}, 0.0

    try:
        out, err = proc.communicate(input=json.dumps(task).encode(),
                                    timeout=timeout)
    except subprocess.TimeoutExpired:
        proc.kill()
        try:
            proc.communicate(timeout=5)
        except Exception:
            pass
        return {"id": task_id,
                "error": "timeout after %ss (solver hung)" % timeout}, \
            time.time() - t0
    except Exception as e:
        try:
            proc.kill()
        except Exception:
            pass
        return {"id": task_id, "error": "runner error: %s" % e}, \
            time.time() - t0

    elapsed = time.time() - t0
    # First JSON line with the matching id wins; noise lines are skipped.
    try:
        text = out.decode("utf-8", errors="replace")
    except Exception:
        text = ""
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            obj = json.loads(line)
        except Exception:
            continue
        if isinstance(obj, dict) and obj.get("id") == task_id:
            if "answer" in obj and not isinstance(obj["answer"], str):
                obj["answer"] = str(obj["answer"])
            return obj, elapsed
    err_tail = ""
    try:
        err_tail = err.decode("utf-8", errors="replace")[-300:]
    except Exception:
        pass
    return {"id": task_id,
            "error": "no valid result line from solver"
                     + ("; stderr: " + err_tail if err_tail.strip() else "")}, \
        elapsed


def run_solver(solver_path, tasks, timeout_per_task=10, use_cache=True,
               workers=4):
    """Run solver against tasks in isolated sandboxes, in parallel.

    Returns (answers, meta): answers maps task_id -> {"id","answer"} or
    {"id","error"}; meta has per-task timings and used_bwrap=True.

    use_cache=False binds a fresh empty cache dir so repeated samples are
    independent model calls (M2 fitness sampling).

    workers=4: concurrent sandboxes. Each task is independent (own bwrap,
    own pipes); the shared surfaces are concurrency-safe (call log uses
    flock, cache appends are small O_APPEND writes, rotation uses flock).
    Model calls spread across the provider rotation, so 8 workers stay
    within free-tier rate limits.
    """
    _ensure_bwrap()
    solver_path = os.path.abspath(solver_path)
    if not os.path.isfile(solver_path):
        raise FileNotFoundError("solver not found: %s" % solver_path)
    here = os.path.dirname(os.path.abspath(__file__))
    entry_path = os.path.join(here, _ENTRY_NAME)
    if not os.path.isfile(entry_path):
        raise FileNotFoundError("sandbox entry script missing: %s" % entry_path)
    for p, what in ((_SKILLS_DIR, "skills dir"), (_KNOWLEDGE_DIR, "knowledge dir"),
                    (_OPENROUTER_DIR, "openrouter dir"),
                    (_SKILL_CREATOR_BIN, "skill-creator bin"),
                    (_EGRESS_TLS, "egress TLS bundle")):
        if not os.path.isdir(p):
            raise RuntimeError("sandbox bind source missing: %s (%s)" % (p, what))

    # The solver's response cache must live somewhere writable in the sandbox.
    # Bind a dedicated dir (never the repo) so the cache persists across runs
    # without exposing anything else. use_cache=False (M2 fitness sampling)
    # binds a fresh temp dir so samples are independent model calls.
    if use_cache:
        cache_dir = os.path.join(here, "..", "loop", ".solver_sandbox_cache")
        cache_dir = os.path.normpath(cache_dir)
        os.makedirs(cache_dir, exist_ok=True)
    else:
        cache_dir = tempfile.mkdtemp(prefix="solver_nocache_")
    cache_file = os.path.join(cache_dir, ".solver_cache.jsonl")
    if not os.path.exists(cache_file):
        open(cache_file, "a").close()
    # The solver computes its cache path as ~/workspace/rsi-lab/loop/... via
    # expanduser; inside the sandbox HOME=/sandbox-home, so symlink the name
    # it expects... simpler: tell the truth in meta. The cache key includes
    # the solver's own bytes, so a fresh cache dir is safe (just cold).
    meta_cache = cache_file

    answers = {}
    meta = {"timings": {}, "used_bwrap": True,
            "timeout_per_task": timeout_per_task,
            "workers": workers,
            "network": "shared (solver calls model APIs)",
            "sandbox_cache": meta_cache,
            "cache_precheck_hits": 0}
    if not tasks:
        return answers, meta
    # Phase 1: in-process cache pre-check — skip the sandbox entirely on a
    # hit. This is what makes warm re-grading sub-second. Safe fallback:
    # any miss (or replica drift) just runs the sandbox as before.
    pending = []
    if use_cache and os.path.exists(cache_file):
        for task in tasks:
            prompt, text, usage = _cache_lookup(solver_path, cache_file, task)
            if text is not None:
                task_id = task.get("id")
                _log_cache_hit(task_id, prompt, text, usage)
                answers[task_id] = {"id": task_id, "answer": text}
                meta["timings"][task_id] = 0.0
                meta["cache_precheck_hits"] += 1
            else:
                pending.append(task)
    else:
        pending = list(tasks)
    # Phase 2: sandbox only what the cache didn't cover.
    if not pending:
        return answers, meta
    with ThreadPoolExecutor(
            max_workers=min(workers, len(pending))) as pool:
        future_of = {
            pool.submit(_run_one_task, solver_path, entry_path, cache_file,
                        task, timeout_per_task): task
            for task in pending
        }
        for future, task in future_of.items():
            task_id = task.get("id")
            try:
                result, elapsed = future.result()
            except Exception as e:  # worker itself blew up — never lose a task
                result = {"id": task_id, "error": "worker error: %s" % e}
                elapsed = 0.0
            answers[task_id] = result
            meta["timings"][task_id] = round(elapsed, 3)
    return answers, meta
