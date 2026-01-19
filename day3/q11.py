# Ask the user for a string and print:
# Q10:
# All unique characters
# The count of unique characters


string = input("enter the string")

set = set()

for ch in string:
    set.add(ch)

print(set)
print(len(set))