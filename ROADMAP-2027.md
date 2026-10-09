# RSI Lab Roadmap: thinking into 2027

Written 2026-10-09. This is the forward projection — where the generations go,
what each era demands, and what we pull forward into the present so we arrive faster.

## Era 0 — Infrastructure (gen 1–3, Oct 2026, NOW)
Score stuck ~40–47% on dev. The wins are not score; they are machinery:
noise-margin keep rule, leader review gate, quality filter, efficiency law,
collective mind, teaching catalogs, call logging. Status: DONE.

## Era 1 — Knowledge goes live (gen 4–15, Nov–Dec 2026)
The solver starts writing KNOWLEDGE PLANs citing catalog tags before every task.
Math sits at 0% — the single biggest lever, and it is knowledge-bound, not
reasoning-bound, so it lifts first. Expect the first kept changes here:
better solver prompts, smarter answer parsing, per-suite strategies.
Target: 55–65% on dev.

## Era 2 — The solver rewrites itself (gen 15–40, Q1 2027)
The loop starts improving solver.py structurally: retry logic, task-type
routing, ensemble checks. Diminishing returns on the 15-task dev set begin;
overfitting risk rises. Countermeasures (built now, not later):
- Frozen held-out set (`harness/heldout.json`) — never used for loop decisions.
- Periodic full-140 validation runs.
- Moving-average score tracking, not single-point worship.

## Era 3 — Trajectories become a model (Q1–Q2 2027)
Every kept change is a verified trace: task → knowledge plan → leader
correction → diff → measured score delta. With 100+ kept trajectories,
fine-tune a small open-weights model (7–8B) with LoRA on the winning traces.
The fine-tuned model becomes the new solver brain: faster, cheaper, and it
internalizes what the loop discovered instead of rediscovering it every run.

## Era 4 — The collective compresses (Q2–Q3 2027)
The loop now improves the fine-tuned model's scaffolding and prompts.
Distillation: 19 voices compress into fewer, stronger ones. The pattern
graph ("the wall") starts generating cross-domain invention proposals —
new techniques born from connected patterns, each tested in the harness.
Nothing is invented from thin air; every proposal traces its roots through
the pattern graph.

## Era 5 — Honest eval (H2 2027)
Full evaluation on the frozen held-out set, untouched since Oct 2026.
If the curve held through Eras 1–4, that is the evidence base for the
long-term aim: an AI built by honest search, better than the frontier.

## Failure modes, pre-empted now
1. **Dev-set overfitting** → held-out freeze (this doc's companion commit).
2. **Score noise** → 1-task margin rule + moving averages.
3. **Free-model churn** (monthly) → re-validate seat assignments on each model refresh.
4. **Reward hacking** → critic + safety + leader gates stay mandatory.
5. **Lost future training data** → trajectory logging starts with the next generation.

## What "thinking it into the future" changed today
- `loop/trajectories/` — every proposal's full trace logged as future training data.
- `harness/heldout.json` — 25 tasks frozen for the 2027 honest eval.
- This roadmap — the eras above are the checklist. When an era's work is
  done, the next one starts; no re-deliberation needed.
