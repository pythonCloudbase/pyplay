import os
import shutil
import sys

if(len(sys.argv)>1):
    folder_dir = sys.argv[1]
else :
    folder_dir = './arrange'


for _, _, files in os.walk(folder_dir):
    print(files)
    file_type = []

    # getting file types
    for file in files:
        file_type.append(file.split(".")[1])
        if not os.path.exists(os.path.join(folder_dir,file_type[-1])):
            os.mkdir(os.path.join(folder_dir,file_type[-1]))

    # file_type = set(file_type)
    # print(file_type)
    
    # putting into folders

    for file in files:
        print(file, file.split(".")[1])
        dest = shutil.move(os.path.join(folder_dir, file), os.path.join(folder_dir, file.split(".")[1]))






