import json
import math
import os
import random

BASE = os.path.dirname(os.path.abspath(__file__))

rng = random.Random(42)

def gen_code_repair_tasks():
    tasks = []
    solutions = {}

    def fam_sum_to_n(i):
        n = 10 + i
        name = "sum_to_n"
        prompt = f"Fix the bug in the starter code. Write a function named `{name}` that returns the sum of all integers from 0 to n inclusive."
        starter = "def sum_to_n(n):\n    total = 0\n    for i in range(n):\n        total += i\n    return total"
        reference = "def sum_to_n(n):\n    total = 0\n    for i in range(n + 1):\n        total += i\n    return total"
        tests = f"assert {name}({n}) == {n * (n + 1) // 2}\nassert {name}(0) == 0\n"
        return prompt, starter, reference, tests

    def fam_count_even(i):
        lst = [i, i + 1, i + 2, i + 3, i + 4]  # 5 consecutive ints: odd/even counts always differ
        want = sum(1 for x in lst if x % 2 == 0)
        name = "count_even"
        prompt = f"Fix the bug in the starter code. Write a function named `{name}` that counts how many even numbers are in the list `nums`."
        starter = "def count_even(nums):\n    count = 0\n    for x in nums:\n        if x % 2 != 0:\n            count += 1\n    return count"
        reference = "def count_even(nums):\n    count = 0\n    for x in nums:\n        if x % 2 == 0:\n            count += 1\n    return count"
        tests = f"assert {name}({lst}) == {want}\nassert {name}([]) == 0\n"
        return prompt, starter, reference, tests

    def fam_factorial(i):
        n = 4 + (i % 4)
        name = "factorial"
        prompt = f"Fix the bug in the starter code. Write a function named `{name}` that returns the factorial of n."
        starter = "def factorial(n):\n    return n * factorial(n - 1)"
        reference = "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)"
        tests = f"assert {name}({n}) == {math.factorial(n)}\nassert {name}(0) == 1\n"
        return prompt, starter, reference, tests

    def fam_subtract(i):
        a, b = 20 + i, 3 + (i % 5)
        name = "subtract"
        prompt = f"Fix the bug in the starter code. Write a function named `{name}` that returns a minus b."
        starter = "def subtract(a, b):\n    return b - a"
        reference = "def subtract(a, b):\n    return a - b"
        tests = f"assert {name}({a}, {b}) == {a - b}\n"
        return prompt, starter, reference, tests

    def fam_get_length(i):
        lst = list(range(1, 2 + (i % 6)))
        name = "get_length"
        prompt = f"Fix the bug in the starter code. Write a function named `{name}` that returns the length of the list `lst`."
        starter = "def get_length(lst):\n    len(lst)"
        reference = "def get_length(lst):\n    return len(lst)"
        tests = f"assert {name}({lst}) == {len(lst)}\n"
        return prompt, starter, reference, tests

    def fam_sort_copy(i):
        lst = [3 + (i % 5), 1, 2 + (i % 3), 0]
        name = "sort_copy"
        prompt = f"Fix the bug in the starter code. Write a function named `{name}` that returns a NEW sorted list without modifying the input list."
        starter = "def sort_copy(lst):\n    lst.sort()\n    return lst"
        reference = "def sort_copy(lst):\n    return sorted(lst)"
        tests = (f"data = {lst}\nassert {name}(data) == {sorted(lst)}\n"
                 f"assert data == {lst}\n")
        return prompt, starter, reference, tests

    def fam_divide(i):
        a = 2 * i + 1  # always odd: // and / never agree
        name = "divide"
        prompt = f"Fix the bug in the starter code. Write a function named `{name}` that returns a divided by b as a float."
        starter = "def divide(a, b):\n    return a // b"
        reference = "def divide(a, b):\n    return a / b"
        tests = f"assert {name}({a}, 2) == {a / 2}\n"
        return prompt, starter, reference, tests

    def fam_sum_list(i):
        lst = [i, i + 1, i + 2]
        name = "sum_list"
        prompt = f"Fix the bug in the starter code. Write a function named `{name}` that returns the sum of all elements in `lst`."
        starter = "def sum_list(lst):\n    total = 1\n    for x in lst:\n        total += x\n    return total"
        reference = "def sum_list(lst):\n    total = 0\n    for x in lst:\n        total += x\n    return total"
        tests = f"assert {name}({lst}) == {sum(lst)}\nassert {name}([]) == 0\n"
        return prompt, starter, reference, tests

    families = [fam_sum_to_n, fam_count_even, fam_factorial, fam_subtract,
                fam_get_length, fam_sort_copy, fam_divide, fam_sum_list]
    for i in range(1, 41):
        prompt, starter, reference, tests = families[(i - 1) % len(families)](i)
        task_id = f"repair-{i:02d}"
        tasks.append({"id": task_id, "suite": "code-repair", "prompt": prompt,
                      "starter": starter, "dev": i <= 5})
        solutions[task_id] = {"reference": reference, "tests": tests}
    return tasks, solutions

def gen_code_gen_tasks():
    tasks = []
    solutions = {}
    families = [
        ("reverse_string", lambda s: s[::-1], "def reverse_string(s):\n    '''Return the reversed string.'''\n    pass"),
        ("filter_even", lambda lst: [x for x in lst if x % 2 == 0], "def filter_even(lst):\n    '''Return a list of even numbers from lst.'''\n    pass"),
        ("sum_of_squares", lambda lst: sum(x**2 for x in lst), "def sum_of_squares(lst):\n    '''Return the sum of squares of elements in lst.'''\n    pass"),
        ("count_words", lambda s: len(s.split()), "def count_words(s):\n    '''Return the number of words in string s.'''\n    pass"),
        ("max_in_list", lambda lst: max(lst), "def max_in_list(lst):\n    '''Return the maximum value in lst.'''\n    pass"),
        ("is_palindrome", lambda s: s == s[::-1], "def is_palindrome(s):\n    '''Return True if s is a palindrome.'''\n    pass"),
        ("factorial", lambda n: 1 if n <= 1 else n * factorial(n - 1), "def factorial(n):\n    '''Return the factorial of n.'''\n    pass"),
        ("fibonacci", lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2), "def fibonacci(n):\n    '''Return the nth Fibonacci number.'''\n    pass"),
        ("dict_sum", lambda d: sum(d.values()), "def dict_sum(d):\n    '''Return the sum of all values in dictionary d.'''\n    pass"),
        ("find_max_index", lambda lst: lst.index(max(lst)), "def find_max_index(lst):\n    '''Return the index of the maximum value in lst.'''\n    pass"),
    ]
    for i in range(1, 41):
        family = families[i % len(families)]
        name, func, starter = family
        task_id = f"gen-{i:02d}"
        prompt = f"Write a function named `{name}` that takes appropriate arguments and returns the correct result."
        # Reference implementations per family
        if name == "reverse_string":
            reference = "def reverse_string(s):\n    return s[::-1]"
        elif name == "filter_even":
            reference = "def filter_even(lst):\n    return [x for x in lst if x % 2 == 0]"
        elif name == "sum_of_squares":
            reference = "def sum_of_squares(lst):\n    return sum(x**2 for x in lst)"
        elif name == "count_words":
            reference = "def count_words(s):\n    return len(s.split())"
        elif name == "max_in_list":
            reference = "def max_in_list(lst):\n    return max(lst)"
        elif name == "is_palindrome":
            reference = "def is_palindrome(s):\n    return s == s[::-1]"
        elif name == "factorial":
            reference = "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)"
        elif name == "fibonacci":
            reference = "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)"
        elif name == "dict_sum":
            reference = "def dict_sum(d):\n    return sum(d.values())"
        elif name == "find_max_index":
            reference = "def find_max_index(lst):\n    return lst.index(max(lst))"
        
        tests = f"assert {name}('hello') == 'olleh'\n" if name == "reverse_string" else \
                f"assert {name}([1, 2, 3, 4, 5]) == [2, 4]\n" if name == "filter_even" else \
                f"assert {name}([1, 2, 3]) == 14\n" if name == "sum_of_squares" else \
                f"assert {name}('hello world') == 2\n" if name == "count_words" else \
                f"assert {name}([1, 5, 3, 9, 2]) == 9\n" if name == "max_in_list" else \
                f"assert {name}('racecar') == True\n" if name == "is_palindrome" else \
                f"assert {name}(5) == 120\n" if name == "factorial" else \
                f"assert {name}(10) == 55\n" if name == "fibonacci" else \
                f"assert {name}({{1: 10, 2: 20, 3: 30}}) == 60\n" if name == "dict_sum" else \
                f"assert {name}([1, 5, 3, 9, 2]) == 3\n"
        
        tasks.append({"id": task_id, "suite": "code-gen", "prompt": prompt, "starter": starter, "dev": i <= 5})
        solutions[task_id] = {"reference": reference, "tests": tests}
    return tasks, solutions

def gen_math_tasks():
    tasks = []
    solutions = {}
    families = [
        ("integer_arithmetic", lambda: f"{rng.randint(1, 100)} + {rng.randint(1, 100)} * {rng.randint(1, 100)}"),
        ("fractions", lambda: f"1/2 + 1/3 + 1/6"),
        ("percentages", lambda: f"What is {rng.randint(10, 90)}% of {rng.randint(1, 10) * 100}?"),
        ("linear_equation", lambda: (lambda x: f"Solve for x: 3x + 7 = {3 * x + 7}")(rng.randint(5, 15))),
        ("gcd_lcm", lambda: f"GCD of {rng.randint(10, 100)} and {rng.randint(10, 100)}"),
        ("modular_arithmetic", lambda: f"{rng.randint(10, 100)} mod {rng.randint(2, 20)}"),
        ("area_perimeter", lambda: f"Area of rectangle with length {rng.randint(5, 20)} and width {rng.randint(5, 20)}"),
    ]
    for i in range(1, 61):
        family = families[i % len(families)]
        task_id = f"math-{i:02d}"
        prompt = family[1]()
        # Compute answer
        if "integer_arithmetic" in str(family):
            parts = prompt.split()
            a, b, c = int(parts[0]), int(parts[2]), int(parts[4])
            answer = str(a + b * c)
        elif "fractions" in str(family):
            answer = "1"
        elif "percentages" in str(family):
            parts = prompt.split()
            pct, num = int(parts[2].rstrip('%')), int(parts[4].rstrip('?'))
            answer = str(pct * num // 100)
        elif "linear_equation" in str(family):
            rhs = int(prompt.split('=')[1].strip())
            answer = str((rhs - 7) // 3)
        elif "gcd_lcm" in str(family):
            import math
            parts = prompt.split()
            a, b = int(parts[2]), int(parts[4])
            answer = str(math.gcd(a, b))
        elif "modular_arithmetic" in str(family):
            parts = prompt.split()
            a, b = int(parts[0]), int(parts[2])
            answer = str(a % b)
        elif "area_perimeter" in str(family):
            parts = prompt.split()
            l, w = int(parts[5]), int(parts[8])
            answer = str(l * w)
        
        tasks.append({"id": task_id, "suite": "math", "prompt": prompt, "starter": prompt, "dev": i <= 5})
        solutions[task_id] = {"reference": answer, "tests": ""}
    return tasks, solutions

def main():
    repair_tasks, repair_solutions = gen_code_repair_tasks()
    gen_tasks, gen_solutions = gen_code_gen_tasks()
    math_tasks, math_solutions = gen_math_tasks()
    
    all_tasks = repair_tasks + gen_tasks + math_tasks
    all_solutions = {**repair_solutions, **gen_solutions, **math_solutions}
    
    with open(os.path.join(BASE, "tasks.json"), "w") as f:
        json.dump(all_tasks, f, indent=2)

    with open(os.path.join(BASE, "solutions.json"), "w") as f:
        json.dump(all_solutions, f, indent=2)

if __name__ == "__main__":
    main()
