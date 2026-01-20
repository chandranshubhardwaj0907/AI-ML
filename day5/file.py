#  file operations

# f = open("day5/sample.txt", "r")
# content = f.read()
# print(content)
# f.close()

f = open("day5/sample.txt", "w")

f.write("This is a sample text file.\n")

f.write("It contains multiple lines of text.\n")
f.write("File operations in Python are easy to understand.\n")
f.close()

# deleting the file
import os
os.remove("day5/sample.txt")