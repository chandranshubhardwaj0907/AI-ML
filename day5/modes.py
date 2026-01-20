# read mode -> r
# write mode -> w
# create new and open for writting -> x
# append mode -> a
# read and write mode -> r+

with open("day5/modes.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This file demonstrates different file modes in Python.\n")
    
# binary mode -> adding 'b' to the mode
with open("day5/modes.txt", "rb") as f:
    content = f.read()
    print(content)    
    
