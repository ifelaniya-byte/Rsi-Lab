#!/usr/bin/env python3
"""Fix the base catalogs: retry math (transient null), expand physics/coding
to 150+ topics each via 'add the missing topics' prompts. Validates counts.

Run in background: python3 knowledge/fix_catalogs.py
"""
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response
sys.path.insert(0, "/home/hatch/workspace/skills/openrouter/bin")
from call_log import log_call, paced_fetch

BASE = os.path.dirname(os.path.abspath(__file__))
LEADER = "nvidia/nemotron-3-super-120b-a12b:free"
TARGET = 150


def ask(prompt, note, max_tokens=12000):
    body = json.dumps({
        "model": LEADER,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=body, headers={"Content-Type": "application/json"})
    add_surrogate_to_request(req, "custom.openrouter",
                             allowed_hosts=("openrouter.ai",))
    resp = paced_fetch(req, timeout=600)
    data = read_json_response(resp)
    text = data["choices"][0]["message"]["content"]
    if not text:
        raise ValueError("empty response from leader")
    usage = data.get("usage") or {}
    log_call(LEADER, "board:catalog", prompt=prompt[:300] + "...",
             response=text[:300] + "...",
             prompt_tokens=usage.get("prompt_tokens"),
             completion_tokens=usage.get("completion_tokens"), note=note)
    return text


def count_topics(path):
    if not os.path.exists(path):
        return 0
    return sum(1 for l in open(path)
               if " | " in l and re.match(r"^[A-Z]+-\d+-\d+ \|", l.strip()))


def existing_tags(path):
    tags = set()
    if os.path.exists(path):
        for l in open(path):
            m = re.match(r"^([A-Z]+-\d+-\d+) \|", l.strip())
            if m:
                tags.add(m.group(1))
    return tags


def retry_math():
    path = os.path.join(BASE, "math.md")
    if count_topics(path) >= TARGET:
        print("SKIP math: already sufficient")
        return
    prompt = (
        "You are the leader of a 19-model AI collective building a "
        "civilization-restart black box of human knowledge. Write the "
        "definitive teaching catalog of mathematics — every major field and "
        "its core topics.\n\n"
        "Cover: arithmetic, algebra (elementary/linear/abstract), geometry "
        "(Euclidean/analytic/differential/algebraic), trigonometry, calculus "
        "(single/multi-variable), real and complex analysis, differential "
        "equations (ODE/PDE), discrete math, combinatorics, graph theory, "
        "number theory, probability, statistics, logic and set theory, "
        "topology, measure theory, numerical methods, optimization, "
        "information theory, game theory, dynamical systems, fractals and chaos.\n\n"
        "Format rules (follow exactly):\n"
        "1. Group topics under field headers like '## 01 Arithmetic'.\n"
        "2. One topic per line, exactly: TAG | topic name | one-line explanation | use-when\n"
        "   e.g. MATH-01-001 | Fractions | Parts of a whole; a/b with b != 0 | Use when dividing quantities\n"
        "3. Number fields 01, 02, ... and topics 001, 002, ... within each field.\n"
        "4. MINIMUM 150 topics. This is a hard requirement — count as you go.\n"
        "5. Output ONLY the catalog, no introduction or conclusion."
    )
    text = ask(prompt, "teaching catalog: math (retry)")
    with open(path, "w") as f:
        f.write(f"# Teaching catalog: mathematics\n# Built by the leader ({LEADER})\n\n{text}")
    print(f"OK  math: {count_topics(path)} topics")


def expand(domain, subject, prefix):
    path = os.path.join(BASE, domain + ".md")
    n = count_topics(path)
    if n >= TARGET:
        print(f"SKIP {domain}: {n} topics already")
        return
    tags = existing_tags(path)
    highest_field = 0
    for t in tags:
        try:
            highest_field = max(highest_field, int(t.split("-")[1]))
        except ValueError:
            pass
    existing = "\n".join(l.strip() for l in open(path)
                         if re.match(r"^[A-Z]+-\d+-\d+ \|", l.strip())) if os.path.exists(path) else ""
    need = TARGET - n
    prompt = (
        f"You are the leader of a 19-model AI collective building a "
        f"civilization-restart black box. Below is the current teaching catalog "
        f"of {subject} with {n} topics. It is TOO THIN — expand it.\n\n"
        f"Your job: write AT LEAST {need} NEW topics covering the major fields "
        f"and subtopics that are missing. Do not repeat existing tags.\n\n"
        f"New fields start at number {highest_field + 1:02d} (header like "
        f"'## {highest_field + 1:02d} Field Name'). Continue topic numbering "
        f"001, 002, ... within each new field. Tag prefix: {prefix}.\n\n"
        f"Format per line exactly: TAG | topic name | one-line explanation | use-when\n"
        f"Output ONLY the new topic lines and new field headers, nothing else.\n\n"
        f"Existing catalog (do not repeat these):\n{existing}"
    )
    text = ask(prompt, f"expand catalog: {domain} (+{need} topics)")
    with open(path, "a") as f:
        f.write("\n\n" + text)
    print(f"OK  {domain}: {n} -> {count_topics(path)} topics")


def main():
    for attempt in range(2):
        try:
            retry_math()
            break
        except Exception as e:
            print(f"math attempt {attempt + 1} failed: {str(e)[:120]}")
    for domain, subject, prefix in [("physics", "physics", "PHYS"),
                                    ("coding", "computer science and programming", "CODE")]:
        try:
            expand(domain, subject, prefix)
        except Exception as e:
            print(f"FAIL expand {domain}: {str(e)[:120]}")
    for d in ("math", "physics", "coding"):
        print(f"final {d}: {count_topics(os.path.join(BASE, d + '.md'))} topics")


if __name__ == "__main__":
    main()
