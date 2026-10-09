#!/usr/bin/env python3
"""File-based genie wish with CORRECT cost logging (mirrors genie.py ask).

Persistent copy: /tmp is ephemeral. Usage:
  python3 wish.py <prompt_file> <budget_usd> <max_tokens> <preset> [kind]
"""
import fcntl
import json as _json
import os
import sys

sys.path.insert(0, "/home/hatch/workspace/skills/openrouter/bin")
import genie  # noqa: F401  (ensures env/limits load)
from genie import (PRESETS, estimate_tokens, load_catalog, paid_spend_week,
                   KEY_WEEKLY_LIMIT, LOG_DIR, post_chat, log_call,
                   _content_text)

PROMPT_FILE = sys.argv[1]
BUDGET = float(sys.argv[2])
MAX_TOKENS = int(sys.argv[3])
PRESET = sys.argv[4]
KIND = sys.argv[5] if len(sys.argv) > 5 else "general"

prompt = open(PROMPT_FILE).read()
spent = paid_spend_week()
remaining = KEY_WEEKLY_LIMIT - spent
budget = min(BUDGET, remaining)
print(f"Weekly: ${spent:.4f} spent of ${KEY_WEEKLY_LIMIT:.2f} "
      f"(${remaining:.4f} left)", flush=True)

pre = PRESETS[PRESET]
in_tok, out_tok = estimate_tokens(prompt, MAX_TOKENS)
pick = None
for m in load_catalog():
    if m["id"] == pre["model"]:
        p = m.get("pricing", {})
        pin = float(p.get("prompt", 0) or 0)
        pout = float(p.get("completion", 0) or 0)
        est = in_tok * pin + out_tok * pout
        pick = {"model": pre["model"], "in_price": pin,
                "out_price": pout, "est_cost": est}
        print(f"Preset '{PRESET}': {pre['model']}", flush=True)
        print(f"Quote: ~{in_tok} in / up to {out_tok} out tokens", flush=True)
        print(f"Budgeted cost: ~${est:.4f} (worst case) vs ${budget:.4f}",
              flush=True)
        break
if pick is None:
    print("Preset model not in catalog.")
    sys.exit(4)
if pick["est_cost"] > budget:
    print("OVER BUDGET — not submitting.")
    sys.exit(3)

lock_path = os.path.join(LOG_DIR, ".genie.lock")
os.makedirs(LOG_DIR, exist_ok=True)
with open(lock_path, "w") as lockf:
    fcntl.flock(lockf, fcntl.LOCK_EX)
    try:
        if paid_spend_week() >= KEY_WEEKLY_LIMIT:
            print("Budget exhausted while waiting.")
            sys.exit(2)
        data, used = post_chat(pick["model"],
                               [{"role": "user", "content": prompt}],
                               max_tokens=MAX_TOKENS,
                               temperature=0.2, timeout=600)
    except Exception as e:
        log_call(pick["model"], f"genie:{KIND}",
                 prompt=prompt[:300] + "...", ok=False,
                 note=f"genie wish failed: {str(e)[:200]}")
        print(f"Wish failed: {e}", file=sys.stderr, flush=True)
        sys.exit(1)
    content = data["choices"][0]["message"]["content"]
    text = _content_text(content)
    _json.dump(data["choices"][0]["message"],
               open(PROMPT_FILE + ".raw.json", "w"))
    usage = data.get("usage") or {}
    pt = usage.get("prompt_tokens") or in_tok
    ct = usage.get("completion_tokens") or 0
    actual = pt * pick["in_price"] + ct * pick["out_price"]
    log_call(used, f"genie:{KIND}", prompt=prompt[:300] + "...",
             response=text[:300] + "...",
             prompt_tokens=pt, completion_tokens=ct,
             note=f"genie wish, budget ${budget:.4f}, actual ${actual:.4f}",
             cost_usd=actual)
    print(f"\n--- answer from {used} (actual cost ${actual:.4f}) ---\n",
          flush=True)
    print(text, flush=True)
    print(f"\n[WISH_DONE ok={bool(text and text.strip())} "
          f"cost={actual:.4f} in={pt} out={ct}]", flush=True)
