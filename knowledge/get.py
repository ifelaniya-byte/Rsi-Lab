#!/usr/bin/env python3
"""Retrieve a topic's catalog entry + black-box depth from the library.

Usage: python3 knowledge/get.py MATH-04-012
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
SEARCH_DIRS = [os.path.join(BASE, "catalogs"), BASE,
               os.path.join(BASE, "blackbox")]


def _read_lines(path):
    with open(path) as f:
        return f.readlines()


def find_catalog_entry(tag):
    for d in SEARCH_DIRS[:2]:
        if not os.path.exists(d):
            continue
        for fn in sorted(os.listdir(d)):  # deterministic, not fs-order
            if not fn.endswith(".md"):
                continue
            for line in _read_lines(os.path.join(d, fn)):
                if line.strip().startswith(tag + " |") or line.strip().startswith(tag + " "):
                    return line.strip(), fn
    return None, None


def find_blackbox_section(tag):
    d = SEARCH_DIRS[2]
    if not os.path.exists(d):
        return None
    for fn in sorted(os.listdir(d)):  # deterministic, not fs-order
        if not fn.endswith(".md"):
            continue
        with open(os.path.join(d, fn)) as f:
            text = f.read()
        m = re.search(rf"^### {re.escape(tag)}\s*\n(.*?)(?=^### |\Z)",
                      text, re.M | re.S)
        if m:
            return m.group(0).strip(), fn
    return None


def main():
    if len(sys.argv) < 2:
        print("usage: get.py TAG  (e.g. get.py MATH-04-012)")
        return
    tag = sys.argv[1].upper()
    entry, fn = find_catalog_entry(tag)
    if entry:
        print(f"[catalog: {fn}]")
        print(entry)
    else:
        print(f"(no catalog entry for {tag})")
    print()
    section = find_blackbox_section(tag)
    if section:
        print(f"[black box: {section[1]}]")
        print(section[0])
    else:
        print("(black-box depth not written yet for this tag)")


if __name__ == "__main__":
    main()
