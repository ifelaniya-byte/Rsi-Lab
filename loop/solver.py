import os
import sys
import json
import urllib.request
import hashlib as _hashlib

# --- Solver response cache -------------------------------------------------
# Key = sha1(solver source + task id + prompt). Grading an unchanged solver
# (e.g. next generation's baseline after 0 kept changes) hits the cache on
# every task: zero model calls, identical grading input. The key binds the
# exact solver code bytes, so a modified solver never sees a stale response.
_SOLVER_CACHE_PATH = os.path.expanduser(
    "~/workspace/rsi-lab/loop/.solver_cache.jsonl")
_solver_cache_mem = None


def _solver_cache_key(task_id, prompt):
    with open(os.path.abspath(__file__), "rb") as f:
        code = f.read()
    h = _hashlib.sha1()
    h.update(code)
    h.update(b"\0" + task_id.encode() + b"\0" + prompt.encode())
    return h.hexdigest()[:24]


def _solver_cache_get(task_id, prompt):
    """Return (text, usage) on hit, (None, None) on miss."""
    global _solver_cache_mem
    if _solver_cache_mem is None:
        _solver_cache_mem = {}
        try:
            with open(_SOLVER_CACHE_PATH) as f:
                for line in f:
                    try:
                        r = json.loads(line)
                        _solver_cache_mem[r["k"]] = (r["t"], r.get("u"))
                    except Exception:
                        pass
        except FileNotFoundError:
            pass
    return _solver_cache_mem.get(_solver_cache_key(task_id, prompt),
                                (None, None))


def _solver_cache_put(task_id, prompt, text, usage=None):
    global _solver_cache_mem
    if _solver_cache_mem is None:
        _solver_cache_mem = {}
    k = _solver_cache_key(task_id, prompt)
    if k in _solver_cache_mem:
        return
    try:
        with open(_SOLVER_CACHE_PATH, "a") as f:
            f.write(json.dumps({"k": k, "t": text, "u": usage}) + "\n")
        _solver_cache_mem[k] = (text, usage)
    except Exception:
        pass


def solve(task):
    """
    Solve a task and return the solution as a string.
    For code tasks: returns code block content.
    For math tasks: returns the answer string.
    """
    # Determine models from environment: cascade of free models, first
    # non-empty answer wins. No single flaky model can stall the loop.
    models = [m.strip() for m in
              os.getenv("SOLVER_MODELS",
                        "poolside/laguna-s-2.1:free,"
                        "nvidia/nemotron-3-super-120b-a12b:free,"
                        "cohere/north-mini-code:free").split(",") if m.strip()]
    if not models:
        models = [os.getenv("SOLVER_MODEL", "poolside/laguna-s-2.1:free")]
    
    # Build prompt — foreplan: decide the answer silently, then emit it tight.
    # No rambling, no restated question, no throat-clearing. Dense output only.
    # Knowledge retrieval: machine-picked catalog entries relevant to the task.
    import sys as _sys
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "..", "knowledge"))
    # Knowledge retrieval is advisory, not load-bearing: a missing or
    # corrupt index must degrade to "no KB entries", never zero the run.
    try:
        from retrieve import retrieve, format_entries
        kb_entries = retrieve(task["prompt"] + "\n" + task.get("starter", ""))
    except Exception:
        kb_entries = []
    kb_block = ""
    if kb_entries:
        kb_block = ("\n\nRELEVANT KNOWLEDGE (cite tags in your plan; ignore what does not apply):\n"
                    + format_entries(kb_entries))
    plan_instr = ("\n\nKNOWLEDGE PLAN (write this first, 2-4 lines): name the catalog tags "
                  "above that this task needs and how you will use each. Then solve.")
    if task["suite"] in ["code-repair", "code-gen"]:
        prompt = (f"{task['prompt']}\n\n```\n{task['starter']}\n```"
                  f"{kb_block}{plan_instr}"
                  "\n\nPlease write the complete, correct code. Only output the code in a single code block.")
    else:  # math
        prompt = (f"{task['prompt']}\n\n{task['starter']}"
                  f"{kb_block}{plan_instr}"
                  "\n\nAfter your plan, work the problem, then put the final answer alone "
                  "on the last line as: ANSWER: <exact answer string>")
    
    # Call OpenRouter API via the shared path
    # (pacing, logging, cheap fallback on free-quota exhaustion)
    # NOTE: the skill bin must be on sys.path BEFORE the cache-hit branch
    # below — it imports call_log too (latent bug found via sandbox: warm
    # cache + missing path insert = ModuleNotFoundError).
    sys.path.insert(0, "/home/hatch/workspace/skills/openrouter/bin")
    cached, cached_usage = _solver_cache_get(task["id"], prompt)
    if cached is not None:
        from call_log import log_call as _lc
        # Log the ORIGINAL token cost so efficiency comparisons stay honest;
        # the ledger excludes api="cache" from spend/quota sums.
        _lc("cache", "loop:solver", prompt=prompt[:300] + "...",
            response=cached[:300] + "...", note="CACHE HIT", api="cache",
            prompt_tokens=(cached_usage or {}).get("prompt_tokens"),
            completion_tokens=(cached_usage or {}).get("completion_tokens"))
        text = cached
    else:
        from call_log import log_call
        from quality import post_chat

        text = ""
        used_model = None
        note = None
        usage = {}
        response_data = {}
        from providers import pick_api, chat as provider_chat, chat_any
        tried_providers = set()
        first_api = pick_api()
        provider_latency = None
        if first_api != "openrouter":
            # Balanced rotation: this call starts on the alternate API
            try:
                text, used_model = provider_chat(
                    first_api, [{"role": "user", "content": prompt}],
                    max_tokens=4000, temperature=0.2)
                if text and text.strip():
                    note = f"BALANCED {first_api}:{used_model}"
                    provider_latency = getattr(provider_chat, "last_latency", None)
                    usage = getattr(provider_chat, "last_usage", None) or {}
                else:
                    text = ""
                    raise RuntimeError(f"{first_api}: empty response")
            except Exception:
                text = ""
                tried_providers.add(first_api)
                first_api = "openrouter"  # fall through to cascade
        if not text and first_api == "openrouter":
            for model_id in models:
                try:
                    response_data, used = post_chat(
                        model_id, [{"role": "user", "content": prompt}],
                        max_tokens=4000, temperature=0.2, timeout=300)
                    cand = response_data["choices"][0]["message"]["content"]
                    if cand and cand.strip():
                        text, used_model = cand, used
                        break
                except Exception:
                    continue
        if not text:
            # Remaining providers (skipping any already tried)
            try:
                text, used_model = chat_any(
                    [{"role": "user", "content": prompt}],
                    max_tokens=4000, temperature=0.2,
                    skip=tried_providers)
                note = f"PROVIDER FALLBACK {used_model}"
                provider_latency = getattr(provider_chat, "last_latency", None)
                usage = getattr(provider_chat, "last_usage", None) or {}
            except Exception as e:
                # Total failure: log it (ok=False) so health scores and
                # the ledger see it; the grader treats "" as wrong.
                log_call(models[0], "loop:solver", prompt=prompt[:300] + "...",
                         ok=False,
                         note=f"all solver providers failed: {str(e)[:150]}")
                return ""
        try:
            usage = response_data.get("usage") or usage
        except Exception:
            pass
        if used_model and used_model != models[0] and note is None:
            note = f"solver cascade used {used_model}"
        log_call(used_model or models[0], "loop:solver", prompt=prompt[:300] + "...",
                 response=text[:300] + "...",
                 prompt_tokens=usage.get("prompt_tokens"),
                 completion_tokens=usage.get("completion_tokens"),
                 note=note,
                 latency_s=(provider_latency or
                            getattr(post_chat, "last_latency", None)),
                 api=(note.split()[1].split(":")[0]
                      if note and (note.startswith("BALANCED") or
                                   note.startswith("PROVIDER"))
                      else "openrouter"),
                 estimated_tokens=bool(usage.get("estimated")))
        _solver_cache_put(task["id"], prompt, text, usage)
    # Extract solution
    if task["suite"] in ["code-repair", "code-gen"]:
        # Extract first fenced code block; fall back to the whole text
        lines = text.split('\n')
        in_code_block = False
        code_lines = []
        found_fence = False
        for line in lines:
            if line.strip().startswith("```"):
                found_fence = True
                if not in_code_block:
                    in_code_block = True
                else:
                    break
            elif in_code_block:
                code_lines.append(line)
        if found_fence:
            return '\n'.join(code_lines).strip()
        return text.strip()
    else:
        # Math task: take the last ANSWER: line; fall back to stripped text
        answer = text.strip()
        for line in reversed(text.split("\n")):
            s = line.strip()
            if s.upper().startswith("ANSWER:"):
                answer = s[len("ANSWER:"):].strip()
                break
        return answer

