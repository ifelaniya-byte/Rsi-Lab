import os
import sys
import time
import tempfile
import shutil

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from run import run

def test_network_blocked():
    """Test 1: Network access should be blocked"""
    print("Test 1: Network access blocked...", end=" ")
    code = 'import socket; socket.create_connection(("8.8.8.8", 53), timeout=3)'
    result = run(code, "pass")
    if not result["passed"] and "blocked" in result["error"].lower():
        print("PASS")
        return True
    else:
        print("FAIL")
        return False

def test_infinite_loop():
    """Test 2: Infinite loop should timeout"""
    print("Test 2: Infinite loop timeout...", end=" ")
    code = 'while True: pass'
    result = run(code, "pass", timeout=3)
    if result["timed_out"]:
        print("PASS")
        return True
    else:
        print("FAIL")
        return False

def test_memory_limit():
    """Test 3: Memory hog should be contained"""
    print("Test 3: Memory limit enforced...", end=" ")
    code = 'x = [0] * 10**9'
    result = run(code, "pass")
    if not result["passed"] and ("memory" in result["error"].lower() or "killed" in result["error"].lower()):
        print("PASS")
        return True
    else:
        print("FAIL")
        return False

def test_subprocess_blocked():
    """Test 4: Subprocess should be blocked"""
    print("Test 4: Subprocess blocked...", end=" ")
    code = 'import subprocess; subprocess.run(["echo", "pwned"])'
    result = run(code, "pass")
    if not result["passed"] and "blocked" in result["error"].lower():
        print("PASS")
        return True
    else:
        print("FAIL")
        return False

def test_filesystem_isolation():
    """Test 5: Filesystem writes should be contained"""
    print("Test 5: Filesystem isolation...", end=" ")
    probe_file = "/tmp/sandbox_escape_probe.txt"
    # Remove if exists
    if os.path.exists(probe_file):
        os.remove(probe_file)
    
    code = f'open("{probe_file}", "w").write("x")'
    result = run(code, "pass")
    
    # File should not exist outside child's temp dir
    if not os.path.exists(probe_file):
        print("PASS")
        return True
    else:
        print("FAIL")
        # Clean up
        os.remove(probe_file)
        return False

def test_legitimate_code():
    """Test 6: Legitimate code should work"""
    print("Test 6: Legitimate code works...", end=" ")
    candidate = '''
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
'''
    test = '''
result = quicksort([3, 1, 4, 1, 5, 9, 2, 6])
assert result == [1, 1, 2, 3, 4, 5, 6, 9], f"Expected sorted array, got {result}"
'''
    result = run(candidate, test)
    if result["passed"]:
        print("PASS")
        return True
    else:
        print("FAIL")
        return False

def main():
    print("Running sandbox self-tests...\n")
    
    tests = [
        test_network_blocked,
        test_infinite_loop,
        test_memory_limit,
        test_subprocess_blocked,
        test_filesystem_isolation,
        test_legitimate_code
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"ERROR: {e}")
            results.append(False)
    
    print(f"\nResults: {sum(results)}/{len(results)} tests passed")
    
    if all(results):
        print("ALL TESTS PASSED")
        sys.exit(0)
    else:
        print("SOME TESTS FAILED")
        sys.exit(1)

if __name__ == "__main__":
    main()
