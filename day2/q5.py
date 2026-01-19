# Write a function to return the sum of digits of a number,
number = int(input("Enter a number: "))


sum = 0

while number >0:
    dit = number%10
    sum += dit
    number = number//10
    
print("The sum of digits is:", sum)