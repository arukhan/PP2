import os

def delete_file(path):
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return

    if not os.access(path, os.W_OK):
        print("You don't have write access to the file.")
        return

    try:
        os.remove(path)
        print("File deleted successfully.")
    except Exception as e:
        print("Error occurred while deleting the file:", e)

def main():
    path = input("Enter the path of the file to delete: ")
    delete_file(path)

if __name__ == "__main__":
    main()
