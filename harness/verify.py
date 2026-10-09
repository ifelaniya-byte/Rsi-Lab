import json
import os

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base_dir, "tasks.json")) as f:
        tasks = json.load(f)
    with open(os.path.join(base_dir, "solutions.json")) as f:
        solutions = json.load(f)
    
    suite_counts = {"code-repair": {"total": 0, "passed": 0}, "code-gen": {"total": 0, "passed": 0}, "math": {"total": 0, "passed": 0}}
    all_passed = True
    
    for task in tasks:
        suite = task["suite"]
        task_id = task["id"]
        solution = solutions[task_id]
        reference = solution["reference"]
        tests = solution["tests"]
        
        suite_counts[suite]["total"] += 1
        
        try:
            # Test reference passes tests
            ns = {}
            exec(reference, ns)
            exec(tests, ns)
            ref_passed = True
        except Exception as e:
            ref_passed = False
            print(f"FAIL: {task_id} - Reference failed tests: {e}")
            all_passed = False
        
        if suite == "code-repair":
            try:
                # Test starter fails tests
                ns = {}
                exec(task["starter"], ns)
                exec(tests, ns)
                starter_passed = True
            except Exception:
                starter_passed = False
            
            if not starter_passed and ref_passed:
                suite_counts[suite]["passed"] += 1
            else:
                if starter_passed:
                    print(f"FAIL: {task_id} - Starter should fail but passed")
                    all_passed = False
                elif not ref_passed:
                    print(f"FAIL: {task_id} - Reference should pass but failed")
                    all_passed = False
        else:
            if ref_passed:
                suite_counts[suite]["passed"] += 1
            else:
                all_passed = False
    
    for suite, counts in suite_counts.items():
        print(f"{suite}: {counts['passed']}/{counts['total']}")
    
    if all_passed:
        print("PASS")
    else:
        print("FAIL")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    exit(main())
