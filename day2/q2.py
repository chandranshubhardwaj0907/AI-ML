# Write a function that takes two integers and and prints all even numbers between them (inclusive).

number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))

def printevennumber(start , end):
    for i in range(start , end+1):
        if i%2 == 0:
            print(i)
            
printevennumber(number1 , number2)
            
            