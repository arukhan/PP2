def write_list_to_file(filename, input_list):
    try:
        with open(filename, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"List successfully written to {filename}.")
    except Exception as e:
        print(f"Error occurred: {e}")

filename = 'justafile.txt' 
my_list = ['my', 'name', 'is', 'aru'] 
write_list_to_file(filename, my_list)
