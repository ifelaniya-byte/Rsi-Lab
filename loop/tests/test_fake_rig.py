import json
import os
import socket
import sys
import tempfile
import shutil
from pathlib import Path

def run_all():
    """Return (name, ok, detail) tuples."""
    # 1. Create a fixture that maps every purpose to "APPROVE"
    fixture = {
        "loop:orchestrator": "APPROVE",
        "loop:leader": "APPROVE",
        "loop:coder": "APPROVE",
        "loop:autodebug": "APPROVE",
        "loop:coder-revise": "APPROVE",
        "loop:ascent/gen1/p0/rung-1": "APPROVE",
        "loop:ascent/gen1/p0/rung-2": "APPROVE",
        "loop:ascent/gen1/p0/rung-3": "APPROVE",
        "loop:ascent/gen1/p0/rung-4": "APPROVE",
        "loop:ascent/gen1/p0/rung-5": "APPROVE",
        "loop:ascent/gen1/p0/rung-6": "APPROVE",
        "loop:ascent/gen1/p0/judge-final-5": "APPROVE",
        "loop:ascent/gen1/p0/judge-final-6": "APPROVE",
    }
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(fixture, f)
        fixture_path = f.name

    # 2. Import controller BEFORE patching socket: the import itself pulls
    # in urllib/ssl, which subclasses socket.socket at import time.
    loop_root = Path(__file__).parent.parent.parent
    sys.path.insert(0, str(loop_root))
    from loop import controller
    from loop.controller import main

    # 2b. Redirect the loop log to a temp file: the test must NEVER append
    # to the production loop.log (a previous version logged a bogus
    # "Starting generation 1" line into production).
    _tmp_logdir = tempfile.mkdtemp(prefix="t_fakelog_")
    _orig_logfile = controller.LOG_FILE
    controller.LOG_FILE = os.path.join(_tmp_logdir, "loop.log")

    # 3. Monkeypatch socket.socket to raise on any instantiation
    original_socket = socket.socket
    def guard(*args, **kwargs):
        raise RuntimeError("Network access blocked in offline test")
    socket.socket = guard

    # 4. Set environment variable
    os.environ['LAB_FAKE_LLM'] = fixture_path

    # 5. Create a temporary loop directory with minimal solver and prompts
    test_loop_dir = tempfile.mkdtemp(prefix='test_loop_')
    test_loop_path = Path(test_loop_dir)
    (test_loop_path / 'solver.py').write_text('def solve(task): return ""')
    (test_loop_path / 'prompts').mkdir()
    (test_loop_path / 'prompts' / 'orchestrator.md').write_text('{{solver_code}}')
    (test_loop_path / 'prompts' / 'coder.md').write_text('{{proposal}}')
    (test_loop_path / 'prompts' / 'leader.md').write_text('{{proposal}}')
    (test_loop_path / 'prompts' / 'critic.md').write_text('')
    (test_loop_path / 'prompts' / 'safety.md').write_text('')
    (test_loop_path / 'prompts' / 'historian.md').write_text('')

    # 6. Run controller.main with --generations 1 --dev (via sys.argv,
    # since main() takes no arguments and parses argv itself).
    import io
    import contextlib

    old_argv = sys.argv
    sys.argv = ["controller.py", "--generations", "1", "--dev"]
    try:
        with contextlib.redirect_stdout(io.StringIO()), \
             contextlib.redirect_stderr(io.StringIO()):
            main()
        ok = True
        detail = "controller completed without raising"
    except Exception as e:
        ok = False
        detail = f"controller raised: {e}"
    finally:
        sys.argv = old_argv
        # Restore socket and the log file
        socket.socket = original_socket
        controller.LOG_FILE = _orig_logfile
        shutil.rmtree(_tmp_logdir, ignore_errors=True)
        os.environ.pop('LAB_FAKE_LLM', None)
        os.unlink(fixture_path)
        shutil.rmtree(test_loop_dir, ignore_errors=True)

    return [("offline_fake_rig", ok, detail)]

if __name__ == "__main__":
    results = run_all()
    all_ok = True
    for name, ok, detail in results:
        if ok:
            print(f"PASS {name}")
        else:
            print(f"FAIL {name}: {detail}")
            all_ok = False
    sys.exit(0 if all_ok else 1)
