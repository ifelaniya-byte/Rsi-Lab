import json
import os
import sys
from typing import Optional, List, Dict, Any

# Configuration
LOOP_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(LOOP_DIR)

# Model IDs from environment (must be free models on OpenRouter)
ORCHESTRATOR_MODEL = os.getenv("ORCHESTRATOR_MODEL", "nvidia/nemotron-3-ultra-550b-a55b:free")
CODER_MODEL = os.getenv("CODER_MODEL", "poolside/laguna-s-2.1:free")
CRITIC_MODEL = os.getenv("CRITIC_MODEL", "cohere/north-mini-code:free")
SAFETY_MODEL = os.getenv("SAFETY_MODEL", "nvidia/nemotron-3.5-content-safety:free")
HISTORIAN_MODEL = os.getenv("HISTORIAN_MODEL", "dots-studio/dots-3-note-preview:free")
LEADER_MODEL = os.getenv("LEADER_MODEL", "nvidia/nemotron-3-super-120b-a12b:free")

# Seat cascades: if a seat's primary model flakes (empty/connection/403),
# fall through to the next. No single flaky model stalls a seat.
_SEAT_CASCADES = {
    "poolside/laguna-s-2.1:free": [
        "poolside/laguna-s-2.1:free",
        "cohere/north-mini-code:free",
        "nvidia/nemotron-3-super-120b-a12b:free"],
    "poolside/laguna-xs-2.1:free": [
        "poolside/laguna-xs-2.1:free",
        "cohere/north-mini-code:free",
        "nvidia/nemotron-3-super-120b-a12b:free"],
    "nvidia/nemotron-3.5-content-safety:free": [
        "nvidia/nemotron-3.5-content-safety:free",
        "nvidia/nemotron-3-super-120b-a12b:free"],
    "dots-studio/dots-3-note-preview:free": [
        "dots-studio/dots-3-note-preview:free",
        "nvidia/nemotron-3-super-120b-a12b:free"],
    "nvidia/nemotron-3-ultra-550b-a55b:free": [
        "nvidia/nemotron-3-ultra-550b-a55b:free",
        "nvidia/nemotron-3-super-120b-a12b:free"],
    "cohere/north-mini-code:free": [
        "cohere/north-mini-code:free",
        "nvidia/nemotron-3-super-120b-a12b:free"],
    "nvidia/nemotron-3-super-120b-a12b:free": [
        "nvidia/nemotron-3-super-120b-a12b:free",
        "cohere/north-mini-code:free"],
}

def _seat_cascade(model_id):
    base = _SEAT_CASCADES.get(model_id, [model_id])
    # Last resort: the cheap paid model. Keeps the loop alive during
    # free-tier outages for ~$0.03/1M tokens (a generation's seat calls
    # cost a fraction of a cent). Imported lazily to avoid cycles.
    try:
        from call_log import FALLBACK_MODEL
        if FALLBACK_MODEL not in base:
            return base + [FALLBACK_MODEL]
    except Exception:
        pass
    return base

def call_model(model_id, prompt, purpose="loop:call", collective=False):
    """Call a language model via OpenRouter API. Every call is logged."""
    if collective:
        try:
            sys.path.insert(0, os.path.join(LOOP_DIR, "..", "message-board"))
            from collective import collective_context
            prompt = collective_context() + "\n\n" + prompt
        except Exception:
            pass
    # Imports for the shared call path (pacing, logging, cheap fallback)
    sys.path.insert(0, "/home/hatch/workspace/skills/openrouter/bin")
    from call_log import log_call
    from quality import post_chat

    try:
        last_err = None
        provider_note = None
        tried_providers = set()
        from providers import pick_api, chat as provider_chat, chat_any
        first_api = pick_api()
        provider_latency = None
        if first_api != "openrouter":
            # Balanced rotation: this call starts on the alternate API
            try:
                text, used_model = provider_chat(
                    first_api, [{"role": "user", "content": prompt}],
                    max_tokens=4000, temperature=0.2)
                if not text or not text.strip():
                    raise RuntimeError(f"{first_api}: empty response")
                response_data = {"usage":
                                 getattr(provider_chat, "last_usage", None) or {}}
                provider_latency = getattr(provider_chat, "last_latency", None)
                provider_note = f"BALANCED {first_api}:{used_model}"
                tried_providers.add(first_api)
            except Exception as e:
                last_err = f"{first_api}: {str(e)[:120]}"
                tried_providers.add(first_api)
                first_api = "openrouter"  # fall through to cascade
        if first_api == "openrouter":
            for mdl in _seat_cascade(model_id):
                try:
                    response_data, used_model = post_chat(
                        mdl, [{"role": "user", "content": prompt}],
                        max_tokens=4000, temperature=0.2, timeout=300)
                    text = response_data["choices"][0]["message"]["content"]
                    if text and text.strip():
                        break
                    last_err = f"empty response from {mdl}"
                except Exception as e:
                    last_err = f"{mdl}: {str(e)[:120]}"
            else:
                # OpenRouter cascade exhausted: try remaining providers
                try:
                    text, used_model = chat_any(
                        [{"role": "user", "content": prompt}],
                        max_tokens=4000, temperature=0.2,
                        skip=tried_providers)
                    response_data = {"usage":
                                     getattr(chat_any, "last_usage", None) or
                                     getattr(provider_chat, "last_usage", None) or {}}
                    provider_latency = getattr(provider_chat, "last_latency", None)
                    provider_note = f"PROVIDER FALLBACK {used_model}"
                except Exception:
                    raise RuntimeError(
                        f"all seat models failed; last: {last_err}")
        usage = response_data.get("usage") or {}
        note = provider_note
        if used_model != model_id and note is None:
            note = f"SEAT CASCADE used {used_model} (primary {model_id} flaked)"
        log_call(used_model, purpose, prompt=prompt, response=text,
                 prompt_tokens=usage.get("prompt_tokens"),
                 completion_tokens=usage.get("completion_tokens"),
                 note=note,
                 latency_s=(provider_latency or
                            getattr(post_chat, "last_latency", None)),
                 api=(provider_note.split()[1].split(":")[0]
                      if provider_note else "openrouter"),
                 estimated_tokens=bool(usage.get("estimated")))
        return text
    except Exception as e:
        log_call(model_id, purpose, prompt=prompt, ok=False,
                 note=f"call failed: {str(e)[:200]}")
        return f"ERROR: {str(e)}"

class FakeLLM:
    def __init__(self, fixture_path: str):
        self.calls: List[Dict[str, Any]] = []
        self.fixture = {}
        if os.path.exists(fixture_path):
            with open(fixture_path, 'r') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self.fixture = data
                else:
                    # Assume it's a list of responses to replay in order
                    self.fixture = {"__replay": data}
        self.replay_index = 0

    def call(self, model_id: str, prompt: str, purpose: str = "loop:call", collective: bool = False) -> str:
        self.calls.append({
            "model_id": model_id,
            "prompt": prompt,
            "purpose": purpose,
            "collective": collective
        })
        if "__replay" in self.fixture:
            if self.replay_index < len(self.fixture["__replay"]):
                resp = self.fixture["__replay"][self.replay_index]
                self.replay_index += 1
                return resp
            return "APPROVE"
        if purpose in self.fixture:
            resp = self.fixture[purpose]
            if isinstance(resp, list):
                if self.replay_index < len(resp):
                    r = resp[self.replay_index]
                    self.replay_index += 1
                    return r
                return "APPROVE"
            return resp
        return "APPROVE"

def get_llm():
    fake_path = os.getenv("LAB_FAKE_LLM")
    if fake_path:
        return FakeLLM(fake_path)
    class RealLLMWrapper:
        def call(self, model_id, prompt, purpose="loop:call", collective=False):
            return call_model(model_id, prompt, purpose, collective)
    return RealLLMWrapper()

def ascent_call_fn():
    """Return a call function compatible with ascent.py's signature."""
    llm = get_llm()
    def adapter(api, models, messages, max_tokens, purpose):
        # Convert messages to a single prompt (ascent uses user-only)
        prompt = messages[0]["content"]
        # Use the first model as model_id (ascent passes a list)
        model_id = models[0] if isinstance(models, list) else models
        # The ascent purpose already includes rung info; pass through.
        response = llm.call(model_id, prompt, purpose=purpose, collective=False)
        return response, f"{api}:{model_id}"
    return adapter
