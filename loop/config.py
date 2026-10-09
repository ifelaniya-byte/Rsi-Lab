import os
import sys
import tomllib

LOOP_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(LOOP_DIR)

# Defaults (current hardcoded values)
LOG_FILE = "/home/hatch/workspace/rsi-lab/logs/loop.log"
SKILLS_DIR = "/home/hatch/workspace/skills"
SECRETS_DIR = "./secrets"

def _resolve_path(path: str) -> str:
    if os.path.isabs(path):
        return path
    return os.path.join(BASE_DIR, path)

def load():
    global LOG_FILE, SKILLS_DIR, SECRETS_DIR
    config_path = os.path.join(BASE_DIR, "lab.toml")
    if not os.path.exists(config_path):
        return  # keep defaults
    try:
        with open(config_path, "rb") as f:
            config = tomllib.load(f)
        if "LOG_FILE" in config:
            LOG_FILE = _resolve_path(config["LOG_FILE"])
        if "SKILLS_DIR" in config:
            SKILLS_DIR = _resolve_path(config["SKILLS_DIR"])
        if "SECRETS_DIR" in config:
            SECRETS_DIR = _resolve_path(config["SECRETS_DIR"])
    except Exception:
        pass  # silent fallback to defaults

# Load on module import
load()
