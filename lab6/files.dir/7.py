def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print(f"Contents of {source_file} copied to {destination_file} successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

source_file = 'justafile.txt'
destination_file = 'anotherfile.txt'
copy_file(source_file, destination_file)
