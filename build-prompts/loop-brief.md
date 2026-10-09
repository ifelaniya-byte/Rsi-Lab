# BUILD BRIEF — Loop component (solver + controller)

You are building the self-improvement loop for an AI lab. Output ONLY complete
file contents, each preceded by a line `# FILE: <relative path>` and nothing
else outside the files. Relative paths are under `loop/`.

## Context you may assume exists (do not rebuild)
- `../harness/tasks.json`: 140 tasks, each {"id","suite","prompt","starter","dev"}.
  Suites: "code-repair" (buggy function in starter), "code-gen" (signature in
  starter), "math" (problem statement in starter, exact answer string expected).
- `../harness/grade.py`: CLI `--solver PATH --tasks {dev|all} --timeout SEC`,
  prints JSON {"total","passed","per_suite":{...},"details":[...]}.
- `../sandbox/run.py`: `run(candidate_code, test_code, timeout=10) ->
  {"passed","error","timed_out"}` — contained execution. You do not call it
  directly; grade.py does.
- OpenRouter API at https://openrouter.ai/api/v1/chat/completions, OpenAI
  chat-completions format. Auth: the machine holds a stored credential; from
  Python do:
  ```python
  import sys
  sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
  from dynamic_credentials import add_surrogate_to_request, read_json_response
  import urllib.request, json
  req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions",
      data=json.dumps({"model": MODEL, "messages": [{"role":"user","content":prompt}],
      "max_tokens": 4000, "temperature": 0.2}).encode(),
      headers={"Content-Type": "application/json"})
  add_surrogate_to_request(req, "custom.openrouter", allowed_hosts=("openrouter.ai",))
  data = read_json_response(urllib.request.urlopen(req, timeout=300))
  text = data["choices"][0]["message"]["content"]
  ```
  Never ask for, print, or store any API key. Use only free models.

## Files to produce

### 1. loop/solver.py
Defines `solve(task) -> str` where task is the public task dict.
- Builds a prompt from task["prompt"] (+ task["starter"] for code tasks),
  calls a free coding model (model id from env SOLVER_MODEL, default
  "poolside/laguna-s-2.1:free"), extracts the code block (strip markdown
  fences) for code tasks or the bare answer for math, returns the string.
- Deliberately simple: clear prompt, one call, light extraction. THIS FILE is
  what the loop will improve in later generations.

### 2. loop/prompts/*.md — one file per seat
- orchestrator.md: proposes up to 3 concrete code changes to solver.py or the
  prompts, each as: what to change, why it should raise the harness score.
- coder.md: turns one proposal into a unified diff against the given file.
- critic.md: reviews a diff that raised the score; rejects cheating
  (hardcoded answers, test-set leakage, disabling tests, weakening asserts).
- safety.md: screens a diff; rejects anything touching files outside solver.py
  and prompts/, anything with network/process/file-system access, anything that
  alters grading or logging.
- historian.md: condenses one generation's events into 5 bullet lines.

### 3. loop/controller.py
CLI: `--generations N --dev` (--dev grades on dev tasks only).
One generation:
1. Baseline: copy solver.py + prompts/ to a scratch dir; grade the copy
   (`python3 ../harness/grade.py --solver <scratch>/solver.py --tasks dev|all`).
2. Orchestrator model proposes ≤3 changes (free reasoning model).
3. Coder model turns each proposal into a unified diff.
4. Apply each diff to the scratch copy; grade; critic + safety review the diffs
   that improved the score.
5. KEEP a diff only if total score strictly increased AND critic AND safety pass.
   Otherwise revert. Copy kept files back over loop/solver.py and loop/prompts/.
6. Append one JSON line per event to /home/hatch/workspace/rsi-lab/logs/loop.log:
   {"ts","gen","event","detail"} with event in
   propose|implement|test|result|keep|revert|safety_block|cheat_flag|milestone;
   include "score" {"code_repair","code_gen","math","total"} on result/keep/
   milestone lines. ts = UTC ISO-8601.

HARD RULES (enforce in code, not just comments):
- Mutable: ONLY the scratch copies, then loop/solver.py and loop/prompts/.
- NEVER write to: ../sandbox/, ../harness/solutions.json, ../harness/tasks.json,
  logs/loop.log except appending JSON lines, controller.py itself.
- If a proposed diff touches a forbidden path, log safety_block and discard it.

Do a static smoke test in your head: imports resolve, CLI parses, prompt files
load. Write clean, stdlib-only Python 3 (urllib, no requests).
