# Write a function that prints the digits of a number,

number = int(input("Enter a number: ")) 

while number > 0:
    digit = number%10
    print(digit)
    number = number//10
    
    