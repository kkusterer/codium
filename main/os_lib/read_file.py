import os
file_name = input("Name of the file w/o '.txt' : ") or "test"
file_extention = input("what is the file extention (.txt, .py) : ") or ".txt"
file = file_name + file_extention
mode = "r"
try:
    with open(file, mode) as file_object:
        content = file_object.read()
        print("Entire file content:")
        print(content)
except:
    ()


