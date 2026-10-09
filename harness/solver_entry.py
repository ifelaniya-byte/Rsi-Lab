"""In-sandbox entry point for M1 solver isolation.

Runs INSIDE the bubblewrap sandbox as uid 65534 with no network and
/home covered. It reads exactly one task JSON object from stdin, imports
/solvers/solver.py, calls solve(task), and prints exactly one JSON line:
  {"id": <task id>, "answer": <str>}   on success
  {"id": <task id>, "error": <str>}    on any failure

Anything the solver prints to stdout is noise to the parent — the parent
takes the first JSON line whose id matches the task.
"""
import importlib.util
import json
import sys
import traceback

SOLVER_PATH = "/solver/solver.py"


def _emit(obj):
    sys.stdout.write(json.dumps(obj) + "\n")
    sys.stdout.flush()


def main():
    try:
        task = json.loads(sys.stdin.read())
    except Exception as e:
        _emit({"id": None, "error": "bad task input: %s" % e})
        return
    task_id = task.get("id") if isinstance(task, dict) else None

    try:
        spec = importlib.util.spec_from_file_location("solver", SOLVER_PATH)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except Exception:
        _emit({"id": task_id,
               "error": "solver import failed: "
                        + traceback.format_exc(limit=3)[-500:]})
        return

    try:
        answer = mod.solve(task)
    except Exception:
        _emit({"id": task_id,
               "error": "solve() raised: "
                        + traceback.format_exc(limit=5)[-500:]})
        return

    if not isinstance(answer, str):
        answer = str(answer)
    _emit({"id": task_id, "answer": answer})


main()
