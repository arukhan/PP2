import functools
import operator

def multiply_list(numbers):
    if not numbers:
        print("The list is empty.")
        return None
    return functools.reduce(operator.mul, numbers)

def main():
    numbers = [int(x) for x in input("Enter the numbers separated by space: ").split()]
    result = multiply_list(numbers)
    if result is not None:
        print("Result of multiplying all numbers:", result)

if __name__ == "__main__":
    main()
