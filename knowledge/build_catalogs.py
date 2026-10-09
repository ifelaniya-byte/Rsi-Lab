#!/usr/bin/env python3
"""Leader builds the three teaching catalogs: math, physics, coding.

Each catalog: every major field and its core topics, one entry per line:
    TAG | topic name | one-line explanation | use-when
Tags are hierarchical: MATH-01-003 = math, field 01, topic 003.

Saves to knowledge/math.md, knowledge/physics.md, knowledge/coding.md.
Run in background: python3 knowledge/build_catalogs.py
"""
import json
import os
import sys
import urllib.request

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response
sys.path.insert(0, "/home/hatch/workspace/skills/openrouter/bin")
from call_log import log_call, paced_fetch

BASE = os.path.dirname(os.path.abspath(__file__))
LEADER = "nvidia/nemotron-3-super-120b-a12b:free"

SPECS = {
    "math": (
        "mathematics",
        "MATH",
        "Cover all major fields: arithmetic, algebra (elementary/linear/abstract), "
        "geometry (Euclidean/analytic/differential/algebraic), trigonometry, calculus "
        "(single/multi-variable), real and complex analysis, differential equations "
        "(ODE/PDE), discrete math, combinatorics, graph theory, number theory, "
        "probability, statistics, logic and set theory, topology, measure theory, "
        "numerical methods, optimization, information theory, game theory, "
        "dynamical systems, fractals and chaos."
    ),
    "physics": (
        "physics",
        "PHYS",
        "Cover all major fields: classical mechanics, electromagnetism, "
        "thermodynamics and statistical mechanics, waves and optics, relativity "
        "(special/general), quantum mechanics, quantum field theory, particle "
        "physics and the Standard Model, condensed matter, fluid dynamics, "
        "astrophysics and cosmology, nuclear physics, plasma physics, "
        "biophysics, and core experimental/lab methods."
    ),
    "coding": (
        "computer science and programming",
        "CODE",
        "Cover all major areas: programming paradigms, data structures, "
        "algorithms (sorting/searching/graph/DP/greedy), complexity theory "
        "(Big-O, P vs NP), systems programming, operating systems, networks, "
        "databases, compilers and languages, concurrency and parallelism, "
        "distributed systems, cryptography and security, machine learning, "
        "software engineering practices (testing, debugging, refactoring, "
        "version control), and development tools."
    ),
}


def build(domain, subject, prefix, coverage):
    prompt = (
        f"You are the leader of a 19-model AI collective. Your task: write the "
        f"definitive teaching catalog of {subject} — every major field and its "
        f"core topics, so every model in the collective can reference it.\n\n"
        f"Coverage must include: {coverage}\n\n"
        f"Format rules (follow exactly):\n"
        f"1. Group topics under field headers like '## 01 Arithmetic'.\n"
        f"2. One topic per line, exactly this shape:\n"
        f"   {prefix}-01-001 | Fractions | Parts of a whole; a/b with b != 0 | Use when dividing quantities or computing ratios\n"
        f"   (TAG | topic name | one-line explanation | use-when, separated by ' | ')\n"
        f"3. Number fields 01, 02, ... and topics 001, 002, ... within each field.\n"
        f"4. Be comprehensive but tight: aim for 150-250 topics total. One line each, no extra prose.\n"
        f"5. Output ONLY the catalog, no introduction or conclusion."
    )
    body = json.dumps({
        "model": LEADER,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 12000,
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
    usage = data.get("usage") or {}
    log_call(LEADER, "board:catalog", prompt=prompt[:300] + "...",
             response=text[:300] + "...",
             prompt_tokens=usage.get("prompt_tokens"),
             completion_tokens=usage.get("completion_tokens"),
             note=f"teaching catalog: {domain}")
    path = os.path.join(BASE, domain + ".md")
    with open(path, "w") as f:
        f.write(f"# Teaching catalog: {subject}\n")
        f.write(f"# Built by the collective leader ({LEADER})\n\n")
        f.write(text)
    n = sum(1 for l in text.splitlines() if " | " in l)
    print(f"OK  {domain}: {n} topics -> {path}")
    return path


def main():
    for domain, (subject, prefix, coverage) in SPECS.items():
        try:
            build(domain, subject, prefix, coverage)
        except Exception as e:
            print(f"FAIL {domain}: {str(e)[:150]}")


if __name__ == "__main__":
    main()
