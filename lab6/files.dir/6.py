import string

def generate_files():
    alphabet = string.ascii_uppercase
    for letter in alphabet:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}")

def main():
    generate_files()
    print("Text files generated successfully.")

if __name__ == "__main__":
    main()
