import os

command = input("what command: ") or "ls -al"
output_file = "file_list.txt"

os.system(f"{command} > {output_file}")

print(f"Output of '{command}' saved to '{output_file}'")
