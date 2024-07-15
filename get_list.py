import os
from os import listdir

def list_files_folders(directory):
    items = os.listdir(directory)
    print (f"Content of '{directory}':")
    for items in items:
        print (items)

if __name__ == "__main__":
    directory_path = input("Enter the Directory_Path: ")
    list_files_folders(directory_path)