#!/usr/bin/env python3
"""Extract `# FILE: <path>` blocks from a model raw-output file.

Usage: extract-files.py <raw-txt> <dest-dir>
Strips markdown fences. Writes each file. Prints the list of files written.
"""
import os
import re
import sys

def main():
    raw_path, dest_dir = sys.argv[1], sys.argv[2]
    with open(raw_path) as f:
        text = f.read()

    # Split on lines that are "# FILE: <path>", optionally preceded by a fence line
    pattern = re.compile(r"(?m)^[ \t]*```[a-zA-Z]*[ \t]*\n[ \t]*# FILE:[ \t]*|^# FILE:[ \t]*")
    splits = pattern.split(text)
    # splits[0] is preamble; the rest alternate path-line-remainder
    written = []
    for chunk in splits[1:]:
        first, _, rest = chunk.partition("\n")
        path = first.strip().strip("`").strip().split()[0] if first.strip() else ""
        if not path or "/" not in path and "." not in path:
            # guard against stray matches; still allow simple names with ext
            if not path:
                continue
        body = re.sub(r"\n[ \t]*```[ \t]*\s*$", "\n", rest)
        body = re.sub(r"^[ \t]*```[a-zA-Z]*[ \t]*\n", "", body)
        dest = os.path.join(dest_dir, path)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w") as f:
            f.write(body)
        written.append(dest)

    for w in written:
        print(w)
    if not written:
        print("NO FILES EXTRACTED", file=sys.stderr)
        sys.exit(1)

main()
