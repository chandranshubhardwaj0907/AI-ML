try:
    x = int(input("Enter numerator: "))
    ans = 10/x
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
else:
    print("The result is:", ans)