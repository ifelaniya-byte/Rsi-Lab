"""Health battery: provider rotation + ledger honesty (no production writes)."""
import json
import os
import sys
import tempfile

sys.path.insert(0, "/home/hatch/workspace/skills/openrouter/bin")
import call_log
import providers


def run_all():
    out = []

    def check(name, cond, detail=""):
        out.append((name, bool(cond), detail))

    # nvidia disabled: chat_any never attempts it
    attempted = []
    orig_chat = providers.chat
    providers.chat = lambda p, m, **k: (attempted.append(p),
                                        (_ for _ in ()).throw(
                                            RuntimeError("x")))[1]
    try:
        providers.chat_any([{"role": "user", "content": "hi"}],
                           max_tokens=5)
    except RuntimeError:
        pass
    finally:
        providers.chat = orig_chat
    check("nvidia skipped", "nvidia-nim" not in attempted, str(attempted))

    # corrupt rotation state doesn't crash the picker
    old_state = providers.ROTATION_STATE
    providers.ROTATION_STATE = tempfile.mktemp(suffix=".json")
    try:
        open(providers.ROTATION_STATE, "w").write('["not","a","dict"]')
        a = providers.pick_api()
        open(providers.ROTATION_STATE, "w").write('{"idx": "nan"}')
        b = providers.pick_api()
        check("corrupt state survives",
              a in providers.API_ROTATION and b in providers.API_ROTATION)
    finally:
        providers.ROTATION_STATE = old_state

    # _record_api hardened
    check("bare BALANCED note",
          providers._record_api({"note": "BALANCED "}) == "openrouter")

    # cost auto-fill + corrupt-line readers, against a TEMP log dir
    old_base = call_log.BASE
    tmp = tempfile.mkdtemp(prefix="t_log_")
    call_log.BASE = tmp
    try:
        c = call_log.estimate_cost("mistralai/mistral-nemo", 10**6, 10**6)
        check("fallback cost priced", c is not None and abs(c - 0.059) < 0.002,
              str(c))
        call_log.log_call("m", "test", prompt_tokens=10,
                          completion_tokens=20)
        with open(call_log._day_file(), "a") as f:
            f.write('{"broken\n')
        s = call_log.summarize()
        r = call_log.recent()
        check("corrupt line survives",
              isinstance(s["used"], int) and isinstance(r, list))
        check("no stub records",
              all('"stub"' not in l for l in open(call_log._day_file())))
    finally:
        call_log.BASE = old_base
    return out


if __name__ == "__main__":
    import shutil
    bad = 0
    for name, ok, detail in run_all():
        print(("PASS " if ok else "FAIL ") + name + (f" [{detail}]" if detail and not ok else ""))
        bad += not ok
    sys.exit(1 if bad else 0)
