#!/usr/bin/env python3
"""Ask all 19 models for their best latest/unproven RSI idea. Saves to research/ideas/.

Run in background: python3 message-board/research_rsi.py
"""
import json
import os
import re
import subprocess
import sys
import urllib.request

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response
sys.path.insert(0, "/home/hatch/workspace/skills/openrouter/bin")
from call_log import log_call, paced_fetch

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(BASE), "research", "ideas")
os.makedirs(OUT, exist_ok=True)

TEAM = [
    ("apodex/apodex-1.1-mini:free", "utility generalist"),
    ("cohere/north-mini-code:free", "code reviewer"),
    ("dots-studio/dots-3-note-preview:free", "historian"),
    ("google/gemma-4-26b-a4b-it:free", "general reasoner"),
    ("google/gemma-4-31b-it:free", "general reasoner"),
    ("google/lyria-3-clip-preview", "audio specialist"),
    ("google/lyria-3-pro-preview", "audio specialist"),
    ("inclusionai/ling-3.1-flash", "fast drafter"),
    ("liquid/lfm-2.5-2.6b:free", "instant checker"),
    ("nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free", "multimodal reasoner"),
    ("nvidia/nemotron-3-super-120b-a12b:free", "tool executor"),
    ("nvidia/nemotron-3-ultra-550b-a55b:free", "orchestrator"),
    ("nvidia/nemotron-3.5-content-safety:free", "safety gate"),
    ("nvidia/nemotron-3.5-lightning:free", "fast iterator"),
    ("openrouter/free", "dispatcher"),
    ("poolside/laguna-s-2.1:free", "coder"),
    ("poolside/laguna-xs-2.1:free", "micro-coder"),
    ("thinkingmachines/inkling-small:free", "fast critic"),
    ("thinkingmachines/inkling:free", "long-memory critic"),
]


def slugify(model_id):
    return re.sub(r"[^a-z0-9]+", "-", model_id.lower()).strip("-")


def ask(model_id, role):
    from collective import collective_context
    prompt = (
        collective_context() + "\n\n"
        + f"You are {model_id} ({role}) on a 19-model AI lab team building a "
        f"self-improving AI system. ASSIGNMENT: bring back your SINGLE best "
        f"latest or unproven idea for recursive self-improvement — an AI "
        f"rewriting its own code to get smarter — especially ideas seen in "
        f"recent Reddit, Twitter/X, or research chatter. Rules: (1) specific "
        f"and actionable, not vague; (2) prefer newer/unproven ideas over "
        f"well-known ones; (3) under 250 words. Format exactly:\n"
        f"IDEA: <name>\nHOW: <mechanism in 2-3 sentences>\n"
        f"WHY: <why it might beat current approaches, 1-2 sentences>"
    )
    body = json.dumps({
        "model": model_id,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 600,
        "temperature": 0.7,
    }).encode()
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=body, headers={"Content-Type": "application/json"})
    add_surrogate_to_request(req, "custom.openrouter",
                             allowed_hosts=("openrouter.ai",))
    resp = paced_fetch(req, timeout=180)
    data = read_json_response(resp)
    text = data["choices"][0]["message"]["content"].strip()
    usage = data.get("usage") or {}
    log_call(model_id, "board:research", prompt=prompt, response=text,
             prompt_tokens=usage.get("prompt_tokens"),
             completion_tokens=usage.get("completion_tokens"))
    return text


def main():
    for model_id, role in TEAM:
        slug = slugify(model_id)
        try:
            text = ask(model_id, role)
            if not text:
                raise ValueError("empty response")
            with open(os.path.join(OUT, slug + ".txt"), "w") as f:
                f.write(f"# {model_id}\n# role: {role}\n\n{text}\n")
            print(f"OK  {slug}")
        except Exception as e:
            print(f"FAIL {slug}: {str(e)[:120]}")


if __name__ == "__main__":
    main()
