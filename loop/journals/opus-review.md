# Opus 5.5 architecture review — 2026-10-09

**Delivery note:** Opus consumed all 2,500 output tokens in reasoning and was
cut off before writing the final structured answer (`content=None`,
`finish_reason=length`). The verdict and three weakest points below are
reconstructed from its complete reasoning trace. The conditional rebuild
branch (exact plan, references, frameworks, for-dummies blueprint) and the
immune-system review did NOT come through — budget left this week (~$0.10)
cannot cover a second wish of this size.

**Cost:** $0.3476 actual (74,394 in / 2,500 out) vs $0.2486 quoted —
the genie's token estimator undercounted input by ~1.5x. Calibration note
filed.

## Verdict: NO — Opus would not build it like this

## The three weakest points

### 1. Unsandboxed execution of mutable solver code (top finding)
The solver artifact runs completely unsandboxed with full privileges in the
grader process — only the *code it generates* is sandboxed, not the solver
itself. Nothing stops it from importing os and reading the sibling
`solutions.json` directly, contradicting the phase1 spec's isolation
requirements. A trivial three-line stub solver could exploit this.

**Verified by Toby 2026-10-09:** cheat solver reading solutions.json at
runtime scored 5/5 on math doing zero work — HOLE PROVEN.
**Shipped:** `diff_reaches_answer_key()` cheat gate in controller.py —
any diff reaching for solutions.json/heldout.json is blocked before it
executes (both the coder path and the revised-diff path). 3 new battery
tests. Proper fix (solve() in a locked-down subprocess) is follow-up work.

### 2. Weak fitness signal
The dev set is 15 tasks; the 140-task set is really ~25 unique problems
(templated families — e.g. the fractions task repeats the identical problem
9 times). The keep gate accepts any single noisy run with no repeated
sampling despite LLM nondeterminism. The "no suite regresses" requirement
from the spec is not implemented — the controller only checks aggregate
totals. The holdout overlaps families with the dev set rather than testing
genuine transfer.

### 3. Ephemeral, soft safety controls
The circuit breaker is an in-memory function attribute — it resets on
process restart, so the "quarantine" claims don't persist. The judges are
free-tier LLMs with raw diff text injected into their prompts (prompt
injection: a diff could claim "APPROVE" outright). The message board that
feeds `collective_context()` into orchestrator/leader/coder prompts is
writable by any of the 19 models — another prompt-injection vector reaching
every seat call.

## Further findings from the trace (unverified)
- Solver cache keys on source text rather than semantics.
- `seed_intros.py` may reference unimported helpers / unpack a string as a
  tuple (file parses OK; runtime path not yet exercised).
- autodebug solver-repair concatenates a diff generated against post-diff
  state onto the original diff — may produce corrupted patches.
- `patch -p1` failing over to `-p0` can leave partial hunks applied,
  silently corrupting the scratch baseline.
- No git/version history when copying patched files back — no real rollback.
- The "curated patch library" in the immune design doc doesn't exist —
  autodebug is freeform LLM repair with a regex classifier (doc-vs-code gap).
- Hardcoded absolute paths; external deps not vendored.

## Immune-system review: NOT DELIVERED (cut off)
## Rebuild blueprint: NOT DELIVERED (cut off)
