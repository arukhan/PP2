import time
import math

def square_root_after_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

def main():
    number = int(input("Enter the number to find square root: "))
    milliseconds = int(input("Enter the delay time in milliseconds: "))
    square_root_after_delay(number, milliseconds)

if __name__ == "__main__":
    main()
