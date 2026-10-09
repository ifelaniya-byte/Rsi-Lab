"""Health battery: message-board channel confinement."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "message-board"))
from board import channel_path, CHANNELS


def run_all():
    out = []

    def check(name, cond, detail=""):
        out.append((name, bool(cond), detail))

    real_channels = os.path.realpath(CHANNELS)
    confined = True
    for evil in ["../x", "../../loop/journals/ascent", "/etc/passwd", ""]:
        try:
            p = channel_path(evil)
            if os.path.dirname(os.path.realpath(p)) != real_channels:
                confined = False
        except ValueError:
            pass
    check("traversal confined", confined)
    check("legit general",
          channel_path("general").endswith("channels/general.md"))
    check("legit openrouter-free",
          channel_path("openrouter-free").endswith(
              "channels/openrouter-free.md"))
    return out


if __name__ == "__main__":
    bad = 0
    for name, ok, detail in run_all():
        print(("PASS " if ok else "FAIL ") + name)
        bad += not ok
    sys.exit(1 if bad else 0)
