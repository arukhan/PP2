import os

def list_directories_files(path):
    dir = []
    files = []

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            dir.append(item)
        else:
            files.append(item)

    return dir, files

def list_all_directories_files(path):
    all_items = []

    for root, dirs, files in os.walk(path):
        for directory in dirs:
            all_items.append(os.path.join(root, directory))
        for file in files:
            all_items.append(os.path.join(root, file))

    return all_items

def main():
    path = input("Enter the path: ")

    directories, files = list_directories_files(path)
    all_items = list_all_directories_files(path)

    print("Directories:")
    for directory in directories:
        print(directory)

    print("\nFiles:")
    for file in files:
        print(file)

    print("\nAll Directories and Files:")
    for item in all_items:
        print(item)

if __name__ == "__main__":
    main()
