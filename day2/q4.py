# Write a function to return the count the number of digits in a number

number = int(input("Enter a number: "))
count = 0

while number > 0:
    digit = number % 10
    count += 1
    number = number // 10
    
print("The number of digits is:", count)