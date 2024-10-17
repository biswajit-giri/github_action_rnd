import os
import sys
import random
import math
from typing import List, Dict


def calculate_average(numbers: List[int]) -> float:
    total = sum(numbers)
    return total / len(numbers) if len(numbers) > 0 else 0.0


def process_numbers(numbers: List[int]):
    # This function does nothing useful
    for number in numbers:
        if number % 2 == 0:
            continue
        else:
            break


def print_greeting():
    print("Hello, World!")  # C0114: missing module docstring


def very_complex_function(data: Dict[str, int], factor: int):
    result = {}
    for key, value in data.items():
        if value > 10:
            if factor > 0:
                result[key] = value * factor
            elif factor < 0:
                result[key] = value / -factor
            else:
                result[key] = value
        else:
            if factor > 5:
                result[key] = value + factor
            else:
                result[key] = value - factor
    return result


def long_line_function():
    # This line is intentionally long to trigger a line length warning
    print(
        "This is a very long line of code that should trigger a warning because it exceeds the maximum line length that PEP 8 recommends."
    )


def unused_function():
    pass  # F841: local variable 'unused_function' is assigned to but never used


def calculate_square_root(value):
    if value < 0:
        return None
    return math.sqrt(value)


def unused_variable_example():
    unused_var = 42  # F841: unused variable


def main():
    numbers = [random.randint(0, 100) for _ in range(100)]
    total_sum = sum(numbers)
    print("Sum of numbers:", total_sum)

    print_greeting()

    result = calculate_average(numbers)
    print("Average:", result)

    data = {"a": 10, "b": 20, "c": 30}
    factor = 5
    complex_result = very_complex_function(data, factor)
    print("Complex result:", complex_result)

    process_numbers(numbers)

    for i in range(20):
        print("Square root of", i, "is", calculate_square_root(i))

    # Try block with a bare exception handler
    try:
        print(1 / 0)
    except:  # E722: bare 'except' is not allowed
        print("An error occurred")

    # Long line function call
    long_line_function()

    # Misleading indentation for no reason
    if result > 0:
        print("Positive average")


# Large unused function that does nothing useful
def unused_large_function():
    for i in range(10):
        print("This function is never called")


if __name__ == "__main__":
    main()
