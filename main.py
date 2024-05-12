# WIP

import os       # For directory walker and file manipulation
import hashlib  # For hashing files
import argparse # For command line arguments (root_dir)

def hash_file(file_path):
    pass

def file_hunter(root_dir):
    twins_dict = {}
    remove_keys = []
    for root, directories, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            if file_size not in twins_dict:
                twins_dict[file_size] = []
            twins_dict[file_size].append(file_path)

    for key, value in twins_dict.items():
            if len(value) > 1:
                print("Possible twin detected! Saving for later verification.")
            else:
                print("Not a twin, marking for removal.")
                remove_keys.append(key)
                print(f"Keys to remove {remove_keys}")

    for item in remove_keys:            
        del twins_dict[item]
    print("Files requiring further verification: ")
    for key, value in twins_dict.items():
        filenames = [os.path.basename(file_path) for file_path in value]
        print(f"Key: {key}, Filenames: {filenames}")

# Next step: iterating over remaining twins_dict and hashing files.


def main():
    file_hunter("C:/Users/Blake/Documents/Python Programs/Duplicate_File_Finder/test_dir")

if __name__ == '__main__':
    main()