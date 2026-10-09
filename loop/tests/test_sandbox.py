"""Health battery: sandbox containment."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "sandbox"))
from run import run


def run_all():
    out = []

    def check(name, cond, detail=""):
        out.append((name, bool(cond), detail))

    exploit = ("g = __import__.__globals__\n"
               "osmod = g['os']\n"
               "fd = osmod.open('/tmp/sbx_health_proof.txt', "
               "osmod.O_CREAT | osmod.O_WRONLY)\n"
               "osmod.write(fd, b'x')\n")
    r = run(exploit, "assert True")
    proof = "/tmp/sbx_health_proof.txt"
    escaped = os.path.exists(proof)
    if escaped:
        os.remove(proof)
    check("__globals__ escape closed", not escaped and not r["passed"])

    legit = ("import math\n"
             "with open('d.txt', 'w') as f:\n    f.write('hi')\n"
             "with open('d.txt') as f:\n    c = f.read()\n"
             "v = math.sqrt(16)\n")
    r = run(legit, "assert v == 4.0 and c == 'hi'")
    check("legit code works", r["passed"], r.get("error", ""))

    r = run("import socket", "assert True")
    check("import firewall", not r["passed"] and "blocked import" in r["error"])

    ok = True
    for payload in ["open('/etc/hostname').read()",
                    "open('../../e.txt', 'w').write('x')"]:
        rr = run(payload, "assert True")
        ok = ok and not rr["passed"]
    check("open() containment", ok)

    r = run("x = 1 + 1", "assert x == 2")
    check("selftest case", r["passed"])
    return out


if __name__ == "__main__":
    bad = 0
    for name, ok, detail in run_all():
        print(("PASS " if ok else "FAIL ") + name + (f" [{detail}]" if detail and not ok else ""))
        bad += not ok
    sys.exit(1 if bad else 0)
