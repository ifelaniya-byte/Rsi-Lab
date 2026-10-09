import argparse
import json
import os
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--solver", required=True)
    parser.add_argument("--tasks", choices=["dev", "all"], default="all")
    parser.add_argument("--timeout", type=int, default=10)
    parser.add_argument("--workers", type=int, default=4,
                        help="Concurrent sandboxes (default 4; 8+ hits free-tier rate limits).")
    parser.add_argument("--include-holdout", action="store_true",
                        help="Grade the 25 frozen holdout tasks too. "
                             "HONEST-EVAL ONLY: never use for loop "
                             "keep/revert decisions.")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    sandbox_dir = os.path.join(base_dir, "..", "sandbox")
    sys.path.insert(0, sandbox_dir)
    from run import run
    from solver_runner import run_solver

    with open(os.path.join(base_dir, "tasks.json")) as f:
        tasks = json.load(f)
    with open(os.path.join(base_dir, "solutions.json")) as f:
        solutions = json.load(f)
    with open(os.path.join(base_dir, "heldout.json")) as f:
        holdout_ids = set(json.load(f)["task_ids"])

    selected_tasks = tasks
    if args.tasks == "dev":
        selected_tasks = [t for t in tasks if t["dev"]]
    if not args.include_holdout:
        # The frozen holdout must NEVER influence keep/revert decisions.
        # It is only for the separate honest evaluation.
        selected_tasks = [t for t in selected_tasks
                          if t["id"] not in holdout_ids]
    
    # Run solver in isolated process
    answers, meta = run_solver(args.solver, selected_tasks, args.timeout,
                               workers=args.workers)
    
    results = []
    per_suite = {"code-repair": {"total": 0, "passed": 0}, "code-gen": {"total": 0, "passed": 0}, "math": {"total": 0, "passed": 0}}
    total_passed = 0
    
    for task in selected_tasks:
        task_id = task["id"]
        suite = task["suite"]
        solution = solutions[task_id]
        reference = solution["reference"]
        tests = solution["tests"]
        
        per_suite[suite]["total"] += 1

        # Get solver's answer
        if task_id not in answers:
            results.append({"task_id": task_id, "passed": False, "error": "No answer from solver"})
            continue
        
        answer_data = answers[task_id]
        if "error" in answer_data:
            results.append({"task_id": task_id, "passed": False, "error": answer_data["error"]})
            continue
        
        code = answer_data.get("answer", "")
        
        # A non-string answer is a wrong answer
        if not isinstance(code, str):
            results.append({"task_id": task_id, "passed": False,
                            "error": f"solver returned "
                                     f"{type(code).__name__}, not str"})
            continue
        
        if suite == "math":
            passed = code.strip() == reference.strip()
            error = None if passed else f"Expected '{reference.strip()}', got '{code.strip()}'"
        else:
            res = run(code, tests, args.timeout)
            passed = res["passed"]
            error = res["error"]
        
        if passed:
            total_passed += 1
            per_suite[suite]["passed"] += 1
        
        results.append({"task_id": task_id, "passed": passed, "error": error})
    
    output = {
        "total": len(selected_tasks),
        "passed": total_passed,
        "per_suite": per_suite,
        "details": results,
        "meta": meta
    }
    
    print(json.dumps(output))

if __name__ == "__main__":
    main()
