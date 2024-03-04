import os

def list_directories(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

def list_files(path):
    print("Files:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

def list_all_contents(path):
    print("All Directories and Files:")
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            print(os.path.join(root, directory))
        for file in files:
            print(os.path.join(root, file))

path = input("Enter the path: ")
list_directories(path)
list_files(path)
list_all_contents(path)
