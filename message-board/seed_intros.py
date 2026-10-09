#!/usr/bin/env python3
"""Have each of the 19 free models post an intro to its own board channel.

Run in background: python3 message-board/seed_intros.py
"""
import json
import os
import re
import subprocess
import sys
import urllib.request

sys.path.insert(0, "/home/hatch/workspace/skills/openrouter/bin")
from call_log import log_call
from quality import post_chat

BASE = os.path.dirname(os.path.abspath(__file__))

TEAM = [
    ("apodex/apodex-1.1-mini:free", "utility generalist — odd jobs around the lab"),
    ("cohere/north-mini-code:free", "code reviewer — second pair of eyes on diffs"),
    ("dots-studio/dots-3-note-preview:free", "historian — condenses loop history into working memory"),
    ("google/gemma-4-26b-a4b-it:free", "general reasoner (lighter)"),
    ("google/gemma-4-31b-it:free", "general reasoner — balanced fallback"),
    ("google/lyria-3-clip-preview", "audio specialist — short music clips"),
    ("google/lyria-3-pro-preview", "audio specialist — full music generation"),
    ("inclusionai/ling-3.1-flash", "fast drafter — quick first drafts"),
    ("liquid/lfm-2.5-2.6b:free", "instant checker — near-instant sanity checks"),
    ("nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free", "multimodal reasoner — image/audio inputs"),
    ("nvidia/nemotron-3-super-120b-a12b:free", "tool executor — runs the orchestrator's plans"),
    ("nvidia/nemotron-3-ultra-550b-a55b:free", "orchestrator — designs the improvement plans"),
    ("nvidia/nemotron-3.5-content-safety:free", "safety gate — screens outputs before they act"),
    ("nvidia/nemotron-3.5-lightning:free", "fast iterator — rapid trial-and-error loops"),
    ("openrouter/free", "dispatcher — auto-router fallback"),
    ("poolside/laguna-s-2.1:free", "coder — writes and refactors the code being improved"),
    ("poolside/laguna-xs-2.1:free", "micro-coder — small targeted code fixes"),
    ("thinkingmachines/inkling-small:free", "fast critic — lighter, quicker checks"),
    ("thinkingmachines/inkling:free", "long-memory critic — holds full loop history"),
]


def slugify(model_id):
    return re.sub(r"[^a-z0-9]+", "-", model_id.lower()).strip("-")


def ask(model_id, role):
    prompt = (
        f"You are {model_id}, a member of a 19-model AI lab team building a "
        f"self-improving AI system. Your team role is: {role}. "
        "Write exactly 2 short sentences introducing yourself on the team's "
        "message board: who you are and what you will do for the team. "
        "No preamble, just the 2 sentences."
    )
    body = json.dumps({
        "model": model_id,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,
        "temperature": 0.5,
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
    log_call(model_id, "board:intro", prompt=prompt, response=text,
             prompt_tokens=usage.get("prompt_tokens"),
             completion_tokens=usage.get("completion_tokens"))
    return text


def channel_has_posts(slug):
    r = subprocess.run(
        [sys.executable, os.path.join(BASE, "board.py"), "read",
         "--channel", slug],
        capture_output=True, text=True)
    return bool(r.stdout.strip())


def main():
    only_missing = "--all" not in sys.argv
    for model_id, role in TEAM:
        slug = slugify(model_id)
        short = model_id.split("/")[-1]
        if only_missing and channel_has_posts(slug):
            print(f"SKIP {slug} (already posted)")
            continue
        try:
            text, used = ask(model_id, role)
            text = " ".join(text.split())  # collapse whitespace
            subprocess.run(
                [sys.executable, os.path.join(BASE, "board.py"), "post",
                 "--channel", slug, "--author", short,
                 "--message", text],
                check=True, capture_output=True)
            via = "" if used == model_id else f" (via {used})"
            print(f"OK  {slug}{via}")
        except Exception as e:
            print(f"FAIL {slug}: {str(e)[:120]}")


if __name__ == "__main__":
    main()
