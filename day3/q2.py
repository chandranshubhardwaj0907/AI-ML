# from tomlkit import string


# . Ask the user for a string and check whether it is a palindrome or not.
# Q1
# A
# is a string which is same when we read it forward & backward. Eg - “madam”, “racecar” etc.
# palindrome
# HINT - A palindrome string is equal to the reversed version of the string. We can use a loop to reverse the string manually. 

string1 = input("Enter a string: ")

reversed_string = ""

for char in string1:
    reversed_string = char + reversed_string
    # print("Reversed string:", reversed_string)    
    if(string1 == reversed_string):
        print(f"{string1} is a palindrome")
    