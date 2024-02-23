def generate_divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def main():
    try:
        n = int(input())
        divisible_numbers = generate_divisible_by_3_and_4(n)
        print(*divisible_numbers, sep=", ")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
