#!/usr/bin/env python3
"""Second-model review pass for wish deliveries (the inner reviewer).

Kilo's Code Reviewer (the "real deal") works on GitHub PRs — it's the right
OUTER gate before merge, but it's PR-based, slow (minutes), and $0.02-0.15+
per review. This is the INNER reviewer: a different model from the coder
checks every delivery against the acceptance brief in seconds, for ~$0.

Usage:
  wish_review.py <wish_out_txt> <brief_txt> [--provider kilo]
               [--model nvidia/nemotron-3-super-120b-a12b:free]

Prints a verdict report. Exit 0 = PASS, 1 = FAIL (blocking defects found).

The reviewer must be a DIFFERENT model family than the coder — the whole
point is independent blind spots (dual-model cross-check). Default reviewer
is Nemotron 3 Ultra (free), matching the model selected for Kilo's GitHub
bot, so both gates think with the same brain.
"""
import re
import sys

sys.path.insert(0, "/home/hatch/workspace/skills/openrouter/bin")
from providers import chat as provider_chat
from call_log import log_call


def extract_files(text):
    parts = re.split(r"^### FILE:\s*(\S+)\s*$", text, flags=re.M)
    files = {}
    for i in range(1, len(parts), 2):
        body = parts[i + 1].split("[WISH_DONE")[0]
        files[parts[i].strip()] = body.strip("\n") + "\n"
    return files


def review_one(path, code, brief, provider, model):
    prompt = (
        "You are a senior code reviewer doing a FINAL check before code is "
        "integrated into a self-improving AI system. Bugs here replicate "
        "themselves. Be strict, be specific, cite line numbers.\n\n"
        "## ACCEPTANCE CRITERIA (the delivery must satisfy ALL of these)\n"
        + brief + "\n\n"
        f"## FILE UNDER REVIEW: {path}\n```\n" + code + "\n```\n\n"
        "## YOUR TASK\n"
        "1. Check EVERY acceptance criterion that applies to THIS file. "
        "Quote the relevant code.\n"
        "2. Hunt for: invented APIs/CLIs that don't exist, wrong JSON keys, "
        "undefined variables, untested code paths, contract mismatches, "
        "silent truncation.\n"
        "3. End with exactly one line: `VERDICT: PASS` or `VERDICT: FAIL`.\n"
        "PASS means the criteria are met and you found no defects in this "
        "file. Anything less is FAIL with defects listed."
    )
    for attempt in range(2):  # one retry on empty (transient flakes)
        try:
            text, used = provider_chat(
                provider, [{"role": "user", "content": prompt}],
                model=model, max_tokens=3000, temperature=0.1, timeout=300)
        except Exception as e:
            log_call(model, "loop:wish-review", prompt=prompt[:300] + "...",
                     ok=False, note=f"reviewer call failed: {str(e)[:150]}")
            return None, f"REVIEWER ERROR on {path}: {e}"
        if text and text.strip():
            break
    else:
        text = None
    if not text or not text.strip():
        log_call(model, "loop:wish-review", prompt=prompt[:300] + "...",
                 ok=False, note=f"reviewer empty response x2: {path}",
                 api=provider)
        return None, f"REVIEWER UNVERIFIABLE on {path}: empty response twice"
    log_call(used or model, "loop:wish-review",
             prompt=prompt[:300] + "...",
             response=text[:300] + "...", api=provider,
             note=f"second-model review pass: {path}")
    return text, None


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        sys.exit(2)
    wish_out, brief_path = args[0], args[1]
    provider = "kilo"
    model = "nvidia/nemotron-3-ultra-550b-a55b:free"
    for i, a in enumerate(args[2:], 2):
        if a == "--provider" and i + 1 < len(args):
            provider = args[i + 1]
        if a == "--model" and i + 1 < len(args):
            model = args[i + 1]

    delivery = open(wish_out).read()
    # Strip the wish trailer — it's metadata, not code.
    delivery = delivery.split("[WISH_DONE")[0]
    brief = open(brief_path).read()
    files = extract_files(delivery)
    if not files:
        print("no ### FILE: blocks found in delivery")
        sys.exit(2)

    overall_fail = False
    for path, code in files.items():
        print(f"\n{'='*60}\nREVIEWING: {path} ({len(code)} chars)\n{'='*60}")
        text, err = review_one(path, code, brief, provider, model)
        if err:
            print(err)
            overall_fail = True
            continue
        print(text or "(empty response)")
        m = re.search(r"VERDICT:\s*(PASS|FAIL)", text or "")
        if not m or m.group(1) == "FAIL":
            overall_fail = True
            if not m:
                print("(no explicit verdict — treating as FAIL)")

    print(f"\n{'='*60}")
    print("OVERALL:", "FAIL" if overall_fail else "PASS")
    sys.exit(1 if overall_fail else 0)


if __name__ == "__main__":
    main()
