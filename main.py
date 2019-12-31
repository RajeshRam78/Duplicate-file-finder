# Project : Duplicate file finder
# Coder   : Rajesh R
# Date    : 29/12/2019


import os
import time
import sys

try:
    os.path.exists(sys.argv[1])
    Root_path = sys.argv[1]
    print("found")
except:
    print("Folder not found")
    time.sleep(1)
    exit()

# class to store the file parameters
class File_tp(object):
    def __init__(self, file_name, file_path):
        self.file_name = file_name
        self.file_path_list = [file_path]
        self.file_size = os.path.getsize(file_path + "\\" +file_name)
        self.file_count = 1


File_object_list = []
Duplicate_count = 0
def find_duplicate_files(Root_path):
    global  Duplicate_count
    # Make file hash table to store the files based on the file's first letter
    File_hash_table = {}

    # Make file hash table to store the file objects based on the file's first letter
    File_objects_hash = {}

    # Create file hash table
    for folder_path, folder_dir, file_names in os.walk(Root_path):
        for file_name in file_names:
            try:
                File_hash_table[file_name[0]].append((file_name, folder_path))
            except:
                File_hash_table[file_name[0]] = [(file_name, folder_path)]

    # list to store the file objects with same starting letter
    File_object_list = []

    # Each hash element in the file hash table
    for hash_element in File_hash_table:
        # Iterate through each element of hash array
        for file_name, folder_path in File_hash_table[hash_element]:
            duplicate = False
            for File_object in File_object_list:
                if file_name == File_object.file_name: # compare if the file name exist already
                    duplicate = (os.path.getsize(folder_path + "\\" + file_name) == File_object.file_size)
                if duplicate:
                    File_object.file_count += 1
                    File_object.file_path_list.append(folder_path)
                    print(File_object.file_count,File_object.file_name)
                    Duplicate_count += 1
                    break
                else:
                    pass
            if not duplicate:
                File_object = File_tp(file_name, folder_path)
                File_object_list.append(File_object)


        File_objects_hash[file_name[0]] = File_object_list



init_time = time.time()
find_duplicate_files(Root_path)
print(time.time() - init_time)

print("Total duplicate files = {}".format(Duplicate_count))



