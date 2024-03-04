import string

def generate_text_files():
    try:
        for letter in string.ascii_uppercase:
            filename = letter + ".txt"
            with open(filename, 'w') as file:
                file.write(f"This is file {filename}.")
        print("Text files created successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

generate_text_files()
