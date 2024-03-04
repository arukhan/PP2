import os

def check_access(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return
    if os.access(path, os.R_OK):
        print(f"You have read access to the path.")
    else:
        print(f"You do not have read access to the path.")
    if os.access(path, os.W_OK):
        print(f"You have write access to the path.")
    else:
        print(f"You do not have write access to the path.")

    if os.access(path, os.X_OK):
        print(f"You have execute access to the path.")
    else:
        print(f"You do not have execute access to the path.")

path = input("Enter the path: ")
check_access(path)
