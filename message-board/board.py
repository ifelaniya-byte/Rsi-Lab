#!/usr/bin/env python3
"""Message board for the 19-model lab team. One channel per model + #general.

Usage:
  board.py post --channel <slug> --author <name> --message "..."
  board.py read --channel <slug> [--last N]
  board.py channels
"""
import argparse
import os
import re
import sys
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
CHANNELS = os.path.join(BASE, "channels")


def slugify(model_id):
    return re.sub(r"[^a-z0-9]+", "-", model_id.lower()).strip("-")


def channel_path(slug):
    """Resolve a channel slug to its file, confined to CHANNELS/.

    The slug is normalized through slugify() so traversal sequences
    ("../", absolute paths) collapse to a harmless flat name, and the
    resolved path is verified to stay inside CHANNELS/ regardless.
    """
    slug = slugify(slug or "")
    if not slug:
        raise ValueError("invalid channel name")
    path = os.path.join(CHANNELS, slug + ".md")
    real = os.path.realpath(path)
    if os.path.dirname(real) != os.path.realpath(CHANNELS):
        raise ValueError("invalid channel name")
    return path


def cmd_post(args):
    os.makedirs(CHANNELS, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # one line per message; escape newlines in the message body
    body = args.message.replace("\n", "\\n")
    line = f"[{ts}] **{args.author}**: {body}\n"
    with open(channel_path(args.channel), "a") as f:
        f.write(line)
    print(f"posted to #{args.channel}")


def cmd_read(args):
    path = channel_path(args.channel)
    if not os.path.exists(path):
        print(f"(no messages in #{args.channel} yet)")
        return
    with open(path) as f:
        lines = [l.rstrip("\n") for l in f if l.strip()]
    # --last 0 means "show none"; lines[-0:] would wrongly show all.
    tail = lines[-args.last:] if args.last > 0 else []
    for line in tail:
        print(line.replace("\\n", "\n"))


def cmd_channels(args):
    if not os.path.exists(CHANNELS):
        print("(no channels yet)")
        return
    for fn in sorted(os.listdir(CHANNELS)):
        if fn.endswith(".md"):
            slug = fn[:-3]
            n = sum(1 for _ in open(os.path.join(CHANNELS, fn)))
            print(f"#{slug} ({n} messages)")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("post")
    p.add_argument("--channel", required=True)
    p.add_argument("--author", required=True)
    p.add_argument("--message", required=True)

    r = sub.add_parser("read")
    r.add_argument("--channel", required=True)
    r.add_argument("--last", type=int, default=20)

    sub.add_parser("channels")
    sub.add_parser("slugify").add_argument("model_id")

    args = ap.parse_args()
    if args.cmd == "post":
        cmd_post(args)
    elif args.cmd == "read":
        cmd_read(args)
    elif args.cmd == "channels":
        cmd_channels(args)
    elif args.cmd == "slugify":
        print(slugify(args.model_id))


if __name__ == "__main__":
    main()
