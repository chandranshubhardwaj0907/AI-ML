# Design a program to continuously input a number from user & print if it is positive or negative until the user enters “Quit”.

while True:
    userinput = input("Enter a number (or type 'Quit' to exit): ")
    if userinput.lower() == "quit":
        break
    number = float(userinput)
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
        
        