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
    time.sleep(5)
    exit()

class File_tp(object):
    def __init__(self, file_name, file_path): #, file_size):
        self.file_name = file_name
        self.file_path_list = [file_path]
        self.file_size = os.path.getsize(file_path + "\\" +file_name)
        self.file_count = 1


File_object_list = []


def find_duplicate_files(Root_path):
    # Collect files as objects
    # if the file_name and size matches , 1) increment file_count ,2) add the duplicate file path to list
    Total_files = len(list(os.walk(os.path.abspath(Root_path))))
    index = 0
    duplicate_count = 0
    for (folder_path, folder_dir, file_names) in (os.walk(Root_path)):
        index += 1
        Percentage = int((index / Total_files) * 100)
        print("Progress: ", Percentage, end="\r")
        for file_name in file_names:
            file_isduplicate = False
            for File_object in File_object_list:
                name_equal = (file_name == File_object.file_name)
                size_equal = (os.path.getsize(folder_path+ "\\" +file_name) == File_object.file_size)
                if name_equal and size_equal:
                    File_object.file_count += 1
                    File_object.file_path_list.append(folder_path)
                    file_isduplicate = True
                    print(File_object.file_count,File_object.file_name)
                    duplicate_count += 1
                    break
                else:
                    pass
            if not file_isduplicate:
                File_object = File_tp(file_name, folder_path)
                File_object_list.append(File_object)

    print(duplicate_count)



init_time = time.time()
find_duplicate_files(Root_path)
print(time.time()-init_time)





