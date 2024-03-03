def write_list_to_file(filename, input_list):
    try:
        with open(filename, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print("List has been written to", filename)
    except IOError:
        print("Error writing to file.")

def main():
    filename = input("Enter the filename to write to: ")
    input_list = input("Enter the elements of the list separated by spaces: ").split()
    write_list_to_file(filename, input_list)

if __name__ == "__main__":
    main()
