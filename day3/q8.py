# Write a program that takes a string from the user and prints the number of spaces in the string.

string = input("Enter a string")

count  = 0

for char in string:
    if char == " ":
        count += 1
        
print("Number of spaces in the string:", count)
         