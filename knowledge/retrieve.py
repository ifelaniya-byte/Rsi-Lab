"""Machine retrieval over the knowledge index.

Given a task prompt, returns the most relevant catalog entries by
keyword overlap. Fast, free, no model call. Used to inject RELEVANT
KNOWLEDGE into solver prompts and to support KNOWLEDGE PLANs.
"""
import json
import os
import re
from collections import Counter

STOP = set("""a an the and or of to in on for with as at by from is are was were
be been being it its this that these those which who whom whose what when
where how why not no nor so such than too very can will just don should now
the task following complete write given code function solve find prove
you your yours we us our ours they them their theirs he him his she her hers
it its there here then than thus hence however also may might must shall
do does did done has have had having get got gets one two three first second
new old all any each every few more most other some only own same into out
up down over under again once here there when where which while who whom
this that these those am an are as at be because been before between both
but buy call came can come could day did each find from get give go had has
her here him himself his how however into itself like look made make many
more most other out part put same seem seen self she than that then there
these they this those through under until use used using want way well went
were what when where which while who will with would your than then""".split())

_INDEX = None
_DF = None  # token -> number of entries containing it
_N = 0


def _load():
    global _INDEX, _DF, _N
    if _INDEX is None:
        here = os.path.dirname(os.path.abspath(__file__))
        _INDEX = json.load(open(os.path.join(here, "index.json")))
        _N = len(_INDEX)
        df = Counter()
        for e in _INDEX.values():
            df.update(set(_tokens(f"{e['topic']} {e['explanation']} {e['use_when']}")))
        _DF = df
    return _INDEX


def _stem(w):
    """Light stemmer: sorts/sorting/sorted -> sort. Applied to both sides."""
    for suf in ("ing", "ed", "es", "s"):
        if len(w) > len(suf) + 3 and w.endswith(suf):
            w = w[: -len(suf)]
            break
    return w


def _tokens(text):
    toks = [_stem(t) for t in re.findall(r"[a-z]{3,}", text.lower())
            if t not in STOP]
    # bigrams capture phrases ("gradient descent", "heat capacity")
    bigrams = [toks[i] + "_" + toks[i + 1] for i in range(len(toks) - 1)]
    return toks + bigrams


# BM25 document stats (built lazily)
_DOC_TOKS = None
_AVGDL = 0.0


def _doc_stats():
    global _DOC_TOKS, _AVGDL
    index = _load()
    if _DOC_TOKS is None:
        _DOC_TOKS = {}
        total = 0
        for tag, e in index.items():
            toks = _tokens(f"{e['topic']} {e['explanation']} {e['use_when']}")
            _DOC_TOKS[tag] = Counter(toks)
            total += len(toks)
        _AVGDL = total / max(1, len(index))
    return _DOC_TOKS


def _idf(tok):
    import math
    return math.log((_N + 1) / (_DF.get(tok, 0) + 1))


def retrieve(task_prompt, top_n=8):
    """BM25 over the knowledge index (terms + bigrams). Fast, free, local."""
    index = _load()
    docs = _doc_stats()
    qtok = Counter(_tokens(task_prompt))
    k1, b = 1.2, 0.75
    scored = []
    nq = len(qtok)
    for tag, dtok in docs.items():
        dl = sum(dtok.values())
        score = 0.0
        matched_terms = 0
        for t, qf in qtok.items():
            tf = dtok.get(t, 0)
            idf = _idf(t)
            if not tf and "_" not in t and len(t) >= 5:
                # substring fallback: "sort" ~ "quicksort"/"sorting"
                for dt, c in dtok.items():
                    if "_" in dt or len(dt) < 5:
                        continue
                    if t in dt or dt in t:
                        tf += 0.5 * c
                        # Weight by the term actually hit. The query term
                        # has df=0, which would score the MAXIMUM idf —
                        # more than an exact match. Weak partials must
                        # never outrank exact hits.
                        idf = _idf(dt)
                        break
            if not tf:
                continue
            matched_terms += 1
            norm = tf * (k1 + 1) / (tf + k1 * (1 - b + b * dl / _AVGDL))
            score += idf * norm
        if score > 0:
            # coverage: entries matching several distinct query terms win
            # over single-word coincidences ("three" -> Triangles)
            coverage = matched_terms / nq
            scored.append((score * (0.3 + 0.7 * coverage), tag))
    scored.sort(reverse=True)
    return [(tag, index[tag]) for _, tag in scored[:top_n]]


def format_entries(entries):
    lines = []
    for tag, e in entries:
        lines.append(f"- {tag} [{e['domain']}] {e['topic']}: {e['explanation']}")
    return "\n".join(lines)


if __name__ == "__main__":
    import sys
    q = sys.stdin.read()
    for tag, e in retrieve(q):
        print(f"{tag} | {e['domain']} | {e['topic']} | {e['explanation']}")
