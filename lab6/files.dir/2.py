import os

def check_path_access(path):
    if not os.path.exists(path):
        print("The path does not exist.")
        return

    print("Path exists.")

    if os.access(path, os.R_OK):
        print("Read access is allowed.")
    else:
        print("No read access.")

    if os.access(path, os.W_OK):
        print("Write access is allowed.")
    else:
        print("No write access.")

    if os.access(path, os.X_OK):
        print("Execute access is allowed.")
    else:
        print("No execute access.")

def main():
    path = input("Enter the path to check: ")
    check_path_access(path)

if __name__ == "__main__":
    main()
