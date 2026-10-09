# FIX BRIEF — harness/gen_tasks.py rewrite

Your gen_tasks.py has bugs. Rewrite ONLY gen_tasks.py from scratch (output it as
`# FILE: harness/gen_tasks.py` and nothing else). These invariants are MANDATORY
— the file will be machine-tested against every one:

1. It must run without errors: `python3 harness/gen_tasks.py` produces
   tasks.json (140 tasks) and solutions.json (140 entries).
2. ONE canonical function name per code task. The name in the prompt, the
   starter code, the reference code, and the tests must be IDENTICAL. (Your last
   version tested `off_by_one(5)` while the code defined `sum_to_n` → NameError.)
3. Test arguments must match the function signature. (Your last version called
   `count_even(5)` with an int on a function that iterates a list → TypeError on
   both buggy and reference.)
4. The buggy starter must FAIL at least one hidden test; the reference must PASS
   all hidden tests. The "buggy" and "reference" must never be inverted.
5. Expected values in tests must be computed by real module-level functions or
   literals — never by a lambda that references a name not defined in its scope.
   (Your `lambda n: ... n * factorial(n - 1)` crashed with NameError.)
6. Keep it deterministic: random.Random(40) — no wait, use seed 42.
7. Same structure as before: 40 code-repair ("repair-01".."repair-40"), 40
   code-gen ("gen-01".."gen-40"), 60 math ("math-01".."math-60"); dev=true for
   the first 5 of each suite. Tasks: {"id","suite","prompt","starter","dev"}.
   Solutions: {"<id>": {"reference","tests"}}; math tests = "" (exact match).

Suggested approach: define each family as a small builder FUNCTION that takes an
index and returns (name, prompt, starter, reference, tests) with all names
consistent, and expected values computed inside that function. Then loop
families to reach the counts.

Output only the file.
