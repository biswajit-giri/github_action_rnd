import random  # Unused import
from typing import List, Dict, Any

def calculate_average(numbers: List[int]) -> float:  # C901 - Function complexity warning
    total = sum(numbers)  # E501 - Line too long
    return total / len(numbers) if numbers else 0.0

def generate_random_numbers(count: int) -> List[int]:  # F841 - Local variable assigned but never used
    return [random.randint(1, 100) for _ in range(count)]  # E501 - Line too long

def process_data(data: Dict[str, Any]) -> None:  # Unused parameter
    if 'values' in data:
        average = calculate_average(data['values'])
        print(f"Average: {average}")
    print("Data processed")  # C901 - Function complexity warning

def main():  # E722 - Do not use bare except
    try:  # Unused exception variable
        numbers = generate_random_numbers(100)
        data = {'values': numbers}
        process_data(data)
    except Exception:  # E722 - Do not use bare except
        pass  # F841 - Local variable assigned but never used

    print("Done processing data.")  # E501 - Line too long
    unused_function()  # Unused function call

def unused_function():
    pass  # F841 - Local variable assigned but never used

if __name__ == "__main__":  # C901 - Function complexity warning
    main()
