import os

file_path = "./gist_dean"

if os.path.isfile(file_path):
    print("File exists")
else:
    print("File doesn't exist")
    with open(file_path, 'w') as open_file:
        open_file.write("Test")