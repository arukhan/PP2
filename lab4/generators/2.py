def generate_even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i

def main():
    try:
        n = int(input())
        even_numbers = generate_even_numbers(n)
        print(*even_numbers, sep=", ")
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()
