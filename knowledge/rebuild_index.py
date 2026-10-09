#!/usr/bin/env python3
"""Rebuild knowledge/index.json from the teaching catalogs.

The index is what retrieve.py actually serves; the catalogs are the
source of truth. Run after any catalog edit:
    python3 rebuild_index.py
Asserts the expected 1,104 unique tags.
"""
import json
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
CATDIR = os.path.join(HERE, "catalogs")
OUT = os.path.join(HERE, "index.json")
EXPECTED = 1104

LINE_RE = re.compile(
    r"^([A-Z]+-\d+-\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*)$")


def main():
    index = {}
    for fn in sorted(os.listdir(CATDIR)):
        if not fn.endswith(".md"):
            continue
        domain = fn[:-3]
        for n, line in enumerate(open(os.path.join(CATDIR, fn)), 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            m = LINE_RE.match(line)
            if not m:
                print(f"SKIP {fn}:{n}: {line[:80]}")
                continue
            tag, topic, expl, use = m.groups()
            if tag in index:
                print(f"DUP {tag} ({fn}:{n}, first in "
                      f"{index[tag]['domain']})")
            index[tag] = {"domain": domain, "topic": topic,
                          "explanation": expl, "use_when": use}
    print("unique tags:", len(index))
    print(Counter(e["domain"] for e in index.values()))
    assert len(index) == EXPECTED, \
        f"expected {EXPECTED} unique tags, got {len(index)}"
    with open(OUT, "w") as f:
        json.dump(index, f, indent=1)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
