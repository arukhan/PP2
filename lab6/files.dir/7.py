def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print("File copied successfully.")
    except IOError:
        print("Error copying file.")

def main():
    source_file = input("Enter the source file: ")
    destination_file = input("Enter the destination file: ")
    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()
