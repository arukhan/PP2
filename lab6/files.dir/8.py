import os

def delete_file(path):
    if not os.access(path, os.F_OK):
        print(f"File at {path} does not exist.")
    elif not os.access(path, os.W_OK):
        print(f"You don't have permission to delete the file at {path}.")
    else:
        try:
            os.remove(path)
            print(f"File at {path} deleted successfully.")
        except Exception as e:
            print(f"Error occurred while deleting file: {e}")

file_path = 'filetodelete.txt'
delete_file(file_path)
