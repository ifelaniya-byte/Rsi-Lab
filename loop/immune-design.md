# IMMUNE SYSTEM — Design Document
*Synthesized from a 6-mind formulation panel (2026-10-09). Five complete
formulations; Gemini's arrived truncated mid-goal.*

## THE GOAL

The Immune System is a continuously running, autonomous "respiratory loop"
over the lab's own codebase: it **inhales** by scanning for bugs,
vulnerabilities, and malicious drift; **holds** by reproducing and
diagnosing each finding in isolation against the lab's journaled history;
and **exhales** by applying bounded, test-verified repairs — recording every
episode (symptom → diagnosis → patch → outcome) so each cycle heals faster
and more correctly than the last. Its sole purpose is to keep the codebase
healthy with zero human-initiated debugging, so the creator spends time
creating, never fixing. *(6/6 converged on this shape; only wording differed.)*

## THE 5 STRONGEST MECHANISMS

1. **Incremental AST-snapshot scanner with a confidence-gated bug queue.**
   Every cycle, snapshot the repo's AST, diff against the previous snapshot,
   and flag new suspicious nodes; only findings at confidence ≥0.85 enter
   the diagnosis queue as normalized reports (file, line, symptom,
   confidence). *(Minds 1, 2, 4, 5, 6 — most unanimous.)*
2. **Sandboxed reproduction + journal-correlated diagnosis.** Reproduce each
   failure in isolation, rank candidate causes by correlating symptoms with
   past journal/notebook episodes; two independent lightweight models
   cross-validate the top hypothesis before any repair. *(Minds 1, 4, 6.)*
3. **Template-library repair with a bounded blast radius.** Repairs come from
   a curated patch library (not freeform codegen), as minimal diffs under a
   hard mutation budget per cycle (e.g. max 3 changes / 30 lines).
   *(Minds 1, 2, 6.)*
4. **Test-gated atomic commit with automatic rollback.** A patch deploys
   only if the full test suite plus regression-baseline pass in the
   sandbox; any failure reverts and logs a regression alert. Significant
   patches are routed through the Ascent deliberation ladder itself — the
   healer judged by the judges. *(Minds 1, 2, 4, 6.)*
5. **Episode journal → regenerative learning loop.** Every heal (and failed
   heal) is journaled and distilled into a notebook lesson, improving future
   detection and template selection. Nightly fine-tuning of the diagnostic
   model is a reserved future stage. *(Minds 1, 2, 4, 6.)*

## TOP RISKS + GUARDRAILS

1. **Bad patch introduces a regression or security flaw** (5/6: #1 risk).
   *Guardrail:* no commit without full-suite + regression-baseline passing;
   automatic rollback; immutable safety-checker with protected paths.
2. **Runaway self-modification** (4/6). *Guardrail:* hard mutation budget
   per cycle + extended circuit breaker — repeated rejected patches trigger
   quarantine mode (log only, healing disabled) until human review resets it.
3. **Overfitting to recent issues** (Mind 4). *Guardrail:* scheduled
   "immune reset" where permanent heuristic changes need human approval.
4. **Healer silently mutates its own code** (Mind 5). *Guardrail:*
   self-modification auditor logs every change to immune-system code.

## THE NEVER LIST

- Never modify, delete, or re-sign anything outside the lab codebase —
  no CI/CD, deployment manifests, or third-party libraries (violation =
  immediate termination + forensic logging).
- Never touch the Ascent's deliberation logic or judge selection, nor the
  circuit breaker's safety thresholds — the judges and the breaker are the
  safety substrate, not heal targets.
- Never modify or delete journals, notebooks, or diagnostic records —
  healing the past is forgery.

## DISAGREEMENTS WORTH PRESERVING

- **Learning weight:** Mind 2 alone wants nightly transformer fine-tuning;
  the rest favor the lighter journal→notebook loop. Ship light first.
- **Human re-approval:** Mind 4 wants monthly "immune reset"; rest rely on
  breaker halts. Compatible: breaker for acute failure, scheduled review
  for chronic drift.
- **NEVER boundary:** directory boundary vs. named subsystems vs.
  memory/journals — merged above as layered prohibitions; all hold.
