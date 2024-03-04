def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print("File not found.")

filename = 'justafile.txt'
num_lines = count_lines(filename)
print(f"Number of lines in {filename}: {num_lines}")