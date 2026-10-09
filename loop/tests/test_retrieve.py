"""Health battery: knowledge index + retrieval."""
import json
import os
import sys

KNOW = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "..", "..", "knowledge")
sys.path.insert(0, KNOW)
from retrieve import retrieve


def run_all():
    out = []

    def check(name, cond, detail=""):
        out.append((name, bool(cond), detail))

    idx = json.load(open(os.path.join(KNOW, "index.json")))
    check("index has 1104 entries", len(idx) == 1104, str(len(idx)))
    for e in idx.values():
        if not all(k in e for k in ("domain", "topic", "explanation",
                                    "use_when")):
            check("index schema", False, "missing keys")
            break
    else:
        check("index schema", True)

    res = retrieve("eigenvalue eigenvector characteristic polynomial")
    check("eigenvalue ranks first",
          res and res[0][1]["topic"].lower().startswith("eigenvalue"),
          res[0][1]["topic"] if res else "no results")
    res = retrieve("sort an array")
    check("sort finds sorting",
          res and "sort" in res[0][1]["topic"].lower(),
          res[0][1]["topic"] if res else "no results")
    return out


if __name__ == "__main__":
    bad = 0
    for name, ok, detail in run_all():
        print(("PASS " if ok else "FAIL ") + name + (f" [{detail}]" if detail and not ok else ""))
        bad += not ok
    sys.exit(1 if bad else 0)
