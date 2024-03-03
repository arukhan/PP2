def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print("File not found.")
        return -1

def main():
    filename = input("Enter the filename: ")
    line_count = count_lines(filename)
    if line_count != -1:
        print("Number of lines in the file:", line_count)

if __name__ == "__main__":
    main()
