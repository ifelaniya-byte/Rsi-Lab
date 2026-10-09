#!/usr/bin/env python3
"""The Black Box: civilization-restart knowledge library (quality-filtered).

Every leader output passes through the Toby-grade quality filter:
machine-validated format, auto-repair on failure. Nothing unvalidated
lands in the library.

Phase A: 5 more teaching catalogs (skips existing).
Phase B: black-box deep volumes for all 8 catalogs (skips existing).

Run in background: python3 knowledge/build_blackbox.py
"""
import os
import re
import sys

sys.path.insert(0, "/home/hatch/workspace/skills/openrouter/bin")
from quality import quality_call

BASE = os.path.dirname(os.path.abspath(__file__))
CATALOGS = os.path.join(BASE, "catalogs")
BLACKBOX = os.path.join(BASE, "blackbox")
LEADER = "nvidia/nemotron-3-super-120b-a12b:free"

NEW_CATALOGS = {
    "chemistry": ("chemistry", "CHEM",
        "atomic structure, periodic table, bonding, stoichiometry, "
        "thermodynamics, kinetics, acids/bases, electrochemistry, organic, "
        "inorganic/materials, analytical methods"),
    "biology": ("biology", "BIO",
        "cell biology, genetics/DNA, evolution, biochemistry, microbiology, "
        "plants/agriculture, human anatomy/physiology, medicine, ecology, "
        "neuroscience"),
    "earth-science": ("earth science", "EARTH",
        "geology, minerals/mining, metallurgy, water, atmosphere/weather, "
        "soil, energy sources, natural resources"),
    "engineering": ("engineering", "ENG",
        "mechanics/structures, tools/machining, construction, electricity, "
        "electronics, engines/machines, manufacturing, measurement, "
        "communication systems"),
    "quantum": ("quantum science", "QUANT",
        "quantum mechanics, entanglement, quantum computing, quantum "
        "cryptography, quantum field theory, particle physics, semiconductors, "
        "quantum sensing, interpretations/frontiers"),
}


def catalog_validator(min_topics):
    def v(text):
        tags = re.findall(r"^[A-Z]+-\d+-\d+ \|", text, re.M)
        issues = []
        if len(tags) < min_topics:
            issues.append(f"only {len(tags)} topics, need at least {min_topics}")
        bad = [l for l in text.splitlines()
               if l.strip() and not l.startswith("#") and not l.startswith("##")
               and " | " in l and not re.match(r"^[A-Z]+-\d+-\d+ \|", l.strip())]
        if bad:
            issues.append(f"{len(bad)} malformed lines, e.g.: {bad[0][:80]}")
        return (not issues, issues)
    return v


def blackbox_validator(expected_tags):
    def v(text):
        issues = []
        found = re.findall(r"^### ([A-Z]+-\d+-\d+)\s*$", text, re.M)
        missing = [t for t in expected_tags if t not in found]
        if missing:
            issues.append(f"missing sections for {len(missing)} topics "
                          f"(e.g. {', '.join(missing[:5])})")
        for tag in found:
            m = re.search(rf"^### {re.escape(tag)}\s*\n(.*?)(?=^### |\Z)",
                          text, re.M | re.S)
            body = m.group(1) if m else ""
            for field in ("PRINCIPLE:", "FORMULAS:", "REBUILD:"):
                if field not in body:
                    issues.append(f"{tag} missing {field}")
                    break
        return (not issues, issues)
    return v


def catalog_topics(path):
    return re.findall(r"^([A-Z]+-\d+-\d+) \|", open(path).read(), re.M)


def phase_a():
    os.makedirs(CATALOGS, exist_ok=True)
    for domain, (subject, prefix, coverage) in NEW_CATALOGS.items():
        path = os.path.join(CATALOGS, domain + ".md")
        if os.path.exists(path):
            print(f"SKIP catalog {domain}: exists")
            continue
        task = (
            f"Write the definitive teaching catalog of {subject} for a "
            f"civilization-restart knowledge library.\n\n"
            f"Coverage must include: {coverage}.\n\n"
            f"Format:\n"
            f"1. Group topics under field headers like '## 01 Atomic Structure'.\n"
            f"2. One topic per line, exactly: TAG | topic name | one-line explanation | use-when\n"
            f"   Example: {prefix}-01-001 | Topic name | One-line explanation | Use-when note\n"
            f"3. Number fields 01, 02, ... and topics 001, 002, ... within each field.\n"
            f"4. MINIMUM 150 topics."
        )
        try:
            text, rep = quality_call(LEADER, task, "board:catalog",
                                     validator=catalog_validator(150),
                                     note=f"teaching catalog: {domain}")
            with open(path, "w") as f:
                f.write(f"# Teaching catalog: {subject}\n# Built by the leader, quality-filtered\n\n{text}")
            print(f"OK  catalog {domain} (repairs: {rep['repairs']})")
        except Exception as e:
            print(f"FAIL catalog {domain}: {str(e)[:150]}")


def phase_b():
    os.makedirs(BLACKBOX, exist_ok=True)
    files = sorted(f for f in os.listdir(CATALOGS) if f.endswith(".md"))
    for fn in files:
        domain = fn[:-3]
        out = os.path.join(BLACKBOX, domain + ".md")
        if os.path.exists(out):
            print(f"SKIP blackbox {domain}: exists")
            continue
        topics = catalog_topics(os.path.join(CATALOGS, fn))
        if not topics:
            print(f"SKIP blackbox {domain}: no topics")
            continue
        chunks = [topics[i:i + 60] for i in range(0, len(topics), 60)]
        parts, failed = [], False
        for ci, chunk in enumerate(chunks):
            listing = "\n".join(chunk)
            task = (
                "Write the BLACK BOX depth for each topic below. Civilization "
                "must be rebuildable from your words alone.\n\n"
                "For EACH topic write exactly:\n"
                "### TAG\n"
                "PRINCIPLE: <core idea in one sentence>\n"
                "FORMULAS: <key equations/laws/rules with symbols, or 'none'>\n"
                "REBUILD: <minimal procedure to use or reconstruct it from scratch>\n\n"
                "Be dense and factual.\n\nTopics (use these exact tags):\n" + listing
            )
            try:
                text, rep = quality_call(
                    LEADER, task, "board:blackbox",
                    validator=blackbox_validator(chunk),
                    note=f"black-box {domain} part {ci + 1}/{len(chunks)}")
                parts.append(text)
                print(f"OK  blackbox {domain} part {ci+1}/{len(chunks)} "
                      f"(repairs: {rep['repairs']})")
            except Exception as e:
                print(f"FAIL blackbox {domain} part {ci+1}: {str(e)[:150]}")
                failed = True
                break
        if not failed:
            with open(out, "w") as f:
                f.write(f"# BLACK BOX volume: {domain}\n# Restart-civilization knowledge. Quality-filtered.\n\n")
                f.write("\n\n".join(parts))
            print(f"OK  blackbox {domain}: {len(topics)} topics deep-written")


def main():
    phase_a()
    phase_b()
    print("black box build done")


if __name__ == "__main__":
    main()
