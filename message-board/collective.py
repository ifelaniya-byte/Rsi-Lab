#!/usr/bin/env python3
"""Collective mind: build the freshest board digest to inject into model prompts.

Every model call gets this block, so each voice has read what the others
said before it speaks. Call it right before each API request — never cache.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
CHANNELS = os.path.join(BASE, "channels")


def _tail(path, n):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        lines = [l.rstrip("\n") for l in f if l.strip()]
    # Unescape \\n like `board.py read` does, so digests don't show
    # literal backslash-n sequences.
    lines = [l.replace("\\n", "\n") for l in lines]
    return lines[-n:] if n > 0 else []


def collective_context(general_last=8, max_chars=1500):
    parts = ["COLLECTIVE MIND — read what your fellow voices said before you answer:"]
    gen = _tail(os.path.join(CHANNELS, "general.md"), general_last)
    if gen:
        parts.append("-- #general --")
        parts.extend(gen)
    others = []
    if os.path.exists(CHANNELS):
        for fn in sorted(os.listdir(CHANNELS)):
            if fn.endswith(".md") and fn[:-3] not in ("general", "scoreboard"):
                last = _tail(os.path.join(CHANNELS, fn), 1)
                if last:
                    others.append(f"[#{fn[:-3]}] {last[0]}")
    if others:
        parts.append("-- voices --")
        parts.extend(others)
    text = "\n".join(parts)
    return text if len(text) <= max_chars else text[:max_chars] + "\n...(truncated)"


if __name__ == "__main__":
    print(collective_context())
