# RSI Lab — Phase 1 Spec: the truth machine + the first loop

Goal: build the harness, the sandbox, and the first self-improvement loop.
No model training in Phase 1. The loop improves the *system's code*, not weights.

## 1. Eval harness (the truth)

Frozen task sets. Nothing in the validation set may be trained on or tuned against —
it is only ever *measured*. A separate small dev set may be used for debugging.

| Suite | What it checks | Size | Pass rule |
|---|---|---|---|
| code-repair | Buggy Python functions; hidden unit tests | 40 tasks | all hidden tests pass |
| code-gen | Write function from spec; hidden tests | 40 tasks | all hidden tests pass |
| math | Numeric/symbolic answers, exact match | 60 tasks | exact answer |
| regression | Previously solved tasks, re-run every generation | grows | no previously-passing task may fail |

Scoring: percent passing per suite + total. A generation "improves" only if the
**total score on the frozen validation set strictly increases** and no suite regresses.

## 2. Sandbox

- Each candidate code change runs inside an isolated container: no network,
  read-only mount of the harness, one writable scratch dir, CPU/memory/time caps.
- The loop's own controller code, the log files, and the sandbox config are
  **outside** the sandbox and read-only to it. The thing being improved can never
  touch its own containment or its own logs.
- Timeouts and crashes count as failures, not retries.

## 3. Loop protocol (one generation)

1. **Orchestrator** proposes up to 3 code changes to the loop's own scaffolding
   (prompts, tool code, search strategy — never the sandbox or logger).
2. **Coder** implements each proposal as a diff.
3. **Sandbox** runs the full harness against each diff, independently.
4. **Critic** reviews the diffs that improved the score, checking for cheating
   (hardcoded answers, test-set leakage, disabled tests).
5. **Safety gate** screens the surviving diff for disallowed behavior.
6. **Keep or revert**: a diff is kept only if validation score strictly increases
   and it passes critic + safety. Everything else is reverted.
7. Every step is appended to `logs/loop.log` as one JSON line (schema in
   `logs/README.md`). Nothing is only-in-memory.

## 4. Seat assignments (first loop, from the 19 free models)

| Seat | Model | Why |
|---|---|---|
| Orchestrator | nvidia/nemotron-3-ultra-550b-a55b:free | strongest reasoning, 1M context, plans the loop |
| Coder | poolside/laguna-s-2.1:free | coding specialist |
| Critic | thinkingmachines/inkling:free | 1M context, holds full history while reviewing |
| Fast checker | liquid/lfm-2.5-2.6b:free | instant sanity checks before full harness runs |
| Safety gate | nvidia/nemotron-3.5-content-safety:free | screens diffs before they are kept |
| Historian | dots-studio/dots-3-note-preview:free | 512K context, condenses generation history |

Bench seats (rotate in if a starter degrades or hits rate limits):
nvidia/nemotron-3-super-120b-a12b:free, nvidia/nemotron-3.5-lightning:free,
cohere/north-mini-code:free, google/gemma-4-31b-it:free.

## 5. Logs and reporting

- `logs/loop.log` — raw JSON-lines event log, written by the loop.
- `logs/milestones.md` — major milestone bullets, maintained by the watcher.
- `logs/README.md` — the exact log schema the loop must follow.
- A scheduled watcher reads new log entries, explains in plain simple language
  what the loop did to improve itself, and appends major milestones
  (first kept self-modification, score breakthroughs, new capability unlocked,
  10/50/100 surviving generations) to `milestones.md`.
