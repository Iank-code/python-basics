# File detection
# import os
#
# path = "/home/mose/Documents/test.txt"
#
# if os.path.exists(path):
#     print("Does exist")
#     if os.path.isfile(path):
#         print("Its indeed a file and not a directory")
#     elif os.path.isdir(path):
#         print("Its indeed not a file but a directory")
# else:
#     print("File does not exist")

# Opening files in python
try:
    with open("test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not fount : (")