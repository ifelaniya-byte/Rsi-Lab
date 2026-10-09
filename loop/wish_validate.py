#!/usr/bin/env python3
"""Post-wish validator: machine-check a model's delivery BEFORE human review.

Catches the failure classes DeepSeek has actually shown:
  - truncated output (hit max tokens mid-file)
  - Python files that don't parse
  - missing expected files
  - [WISH_DONE] ok=False

Usage:
  python3 wish_validate.py <wish_out_txt> <expected_file> [expected_file ...]

Exit 0 = all checks pass. Exit 1 = problems (listed on stdout).
This does NOT check correctness — only that the delivery is complete and
well-formed. Correctness is the reviewer's job (or the test battery's).
"""
import ast
import json
import re
import sys


def extract_files(text):
    parts = re.split(r"^### FILE:\s*(\S+)\s*$", text, flags=re.M)
    files = {}
    for i in range(1, len(parts), 2):
        body = parts[i + 1]
        # Cut everything from the wish trailer onwards (it is not code).
        cut = body.find("[WISH_DONE")
        if cut != -1:
            body = body[:cut]
        files[parts[i].strip()] = body.strip("\n") + "\n"
    return files


def main():
    out_txt = sys.argv[1]
    expected = sys.argv[2:]
    text = open(out_txt).read()
    problems = []

    # 1. Wish-level status
    m = re.search(r"\[WISH_DONE ok=(\w+) cost=([\d.]+) in=(\d+) out=(\d+)\]",
                  text)
    if not m:
        problems.append("no [WISH_DONE] trailer found — output may be truncated")
    else:
        ok, cost, tin, tout = m.group(1), m.group(2), m.group(3), m.group(4)
        if ok != "True":
            problems.append(f"wish reported ok={ok} (cost ${cost})")
        # 2. Truncation heuristic is checked per-file below; the trailer's
        # out= count is informational here.

    files = extract_files(text)

    # 3. Expected files present
    for exp in expected:
        if exp not in files:
            problems.append(f"missing expected file: {exp}")
        elif len(files[exp].strip()) < 50:
            problems.append(f"file suspiciously short (<50 chars): {exp}")

    # 4. Python files parse
    for path, body in files.items():
        if not path.endswith(".py"):
            continue
        # Skip JSON-in-.py mistakes gracefully — just parse.
        try:
            ast.parse(body)
        except SyntaxError as e:
            problems.append(f"{path}: SyntaxError line {e.lineno}: {e.msg}")

    # 5. Truncation: last file ends mid-construct (heuristic)
    if files:
        last_path = list(files.keys())[-1]
        last_body = files[last_path]
        stripped = last_body.rstrip()
        # A complete Python file usually ends with a newline-terminated
        # statement; these endings smell like a cutoff.
        if (stripped.endswith((",", ":", "\\", '"""', "'''"))
                or re.search(r'"[^"\n]*$', stripped)
                or re.search(r"'[^'\n]*$", stripped)):
            problems.append(
                f"{last_path}: ends abruptly — likely truncated by max_tokens")

    if problems:
        print("WISH VALIDATION FAILED:")
        for p in problems:
            print(f"  - {p}")
        return 1
    n_py = sum(1 for p in files if p.endswith(".py"))
    print(f"WISH VALIDATION PASSED: {len(files)} files ({n_py} python, all parse)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
