import os

file_path = '/home/kaleb/codium/fileStuff/example.txt'

if os.path.isfile(file_path):
    print("File exists.")

    with open(file_path , "r") as file:
        content = file.read()
        print(content)

else:
    print("File does not exist (or it is a directory).")