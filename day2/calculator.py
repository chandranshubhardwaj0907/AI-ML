number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Error! Division by zero."
    return a/b

def power(a,b):
    return a**b

operation = input("Choose operation (+, -, *, /, ^): ")

match operation:
    case '+':
        result = add(number1, number2)
    case '-':
        result = subtract(number1, number2)
    case '*':
        result = multiply(number1, number2)
    case '/':
        result = divide(number1, number2)
    case '^':
        result = power(number1, number2)
    case _:
        result = "Invalid operation!"
        
print("The result is:", result)