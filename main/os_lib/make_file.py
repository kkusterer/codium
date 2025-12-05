import os

file_name = input("Name of file( only name not [.txt]) : ") or "test"
file_extention = input("what is the file extention (.txt, .py) : ") or ".txt"

file = file_name + file_extention

mode ="w"

try:
    with open(file, mode) as file:
        file.write("line 1 test as a file object" "\n")
        file.write("line 2 as a test of the file_obj" "\n")
        file.write("line 3 test io os file obj" "\n")
        file.write("line 4 " "\n")

except:
    ()