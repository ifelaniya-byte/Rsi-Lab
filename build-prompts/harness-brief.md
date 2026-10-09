# BUILD BRIEF — Harness component

You are building the eval harness for a self-improving AI lab. Output ONLY complete
file contents, each preceded by a line `# FILE: <relative path>` and nothing else
outside the files. Relative paths are under `harness/`.

## Files to produce

### 1. harness/gen_tasks.py
Generates `tasks.json` and `solutions.json` in the same directory. Must be
deterministic: use `random.Random(42)`.

`tasks.json`: a JSON list of exactly 140 tasks:
- 40 with suite "code-repair", ids "repair-01".."repair-40"
- 40 with suite "code-gen", ids "gen-01".."gen-40"
- 60 with suite "math", ids "math-01".."math-60"

Each task: {"id", "suite", "prompt", "starter", "dev"}.
- "prompt": the exact text shown to the solver model, including the REQUIRED
  function name for code tasks (e.g. "Write a function named `total_cost` ...").
- "starter": code-repair → a buggy Python function (single function, must fail at
  least one hidden test); code-gen → the function signature + docstring only;
  math → the problem statement string (solver must return the exact answer string).
- "dev": true for the first 5 tasks of each suite ("repair-01".."repair-05",
  "gen-01".."gen-05", "math-01".."math-05"), false otherwise.

`solutions.json`: {"<task_id>": {"reference": str, "tests": str}}.
- "reference": correct solution (code tasks: full function source; math: exact
  answer string).
- "tests": code tasks → Python source with `assert` statements referencing the
  candidate's function by its required name. Must PASS on reference, FAIL on the
  buggy starter (for code-repair). Math → empty string (grading is exact match).

Use template families, parameterized to reach the required counts. Examples:
- code-repair families: off-by-one in a loop bound, wrong comparison operator
  (< vs <=), missing base case in recursion, swapped function arguments, forgetting
  to return a value, mutating the input list instead of copying, integer division
  vs float division, wrong initial accumulator value.
- code-gen families: string transformations, list filtering/mapping, simple math
  on numbers, dict aggregation, recursion (factorial-like, fibonacci-like),
  searching/sorting helpers.
- math families: integer arithmetic chains, fractions, percentages, simple linear
  equations (integer solutions), gcd/lcm, modular arithmetic, area/perimeter.

Every task must be unambiguous with exactly one correct answer. No external
packages; stdlib only.

### 2. harness/verify.py
Loads tasks.json + solutions.json. For each task: exec(reference), then
exec(tests) in the same namespace → must pass. For code-repair: exec(starter)
then exec(tests) → must FAIL (proves the bug is real). Print per-suite counts and
a final PASS/FAIL line. Exit 0 only if everything checks out.

### 3. harness/grade.py
CLI: `--solver PATH --tasks {dev|all} --timeout SEC` (timeout default 10).
- Loads the solver module from PATH with importlib (module must define
  `solve(task) -> str`, task is the public task dict).
- For each selected task: `code = solve(task)`.
  - math: passed = (code.strip() == reference.strip()).
  - code: `from run import run` (see sandbox import below), then
    `res = run(code, tests, timeout)`; passed = res["passed"];
    error = res["error"].
- Prints one JSON object to stdout:
  {"total": N, "passed": M, "per_suite": {"code-repair": {"total":..,"passed":..}, ...},
   "details": [{"task_id":.., "passed":..,"error":..}, ...]}

Sandbox import (the sandbox component exposes it; assume it exists):
```python
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sandbox"))
from run import run  # run(candidate_code: str, test_code: str, timeout: int = 10) -> {"passed": bool, "error": str|None, "timed_out": bool}
```

Write clean, working, dependency-free Python 3 code. Think carefully about the
exec-namespace handling in verify.py and grade.py so tests see the candidate's
function.
