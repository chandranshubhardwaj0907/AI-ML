# Letʼs create a “Number Guessing Game”. Given a secret number (already decided by you), write a program that asks the user to guess it and prints:
# •
# if the guess is above the number
# •
# if the guess is below
# •
# if the guess matches

secret_number = 42
guess = int(input("Guess the secret number: "))
if guess < secret_number:
    print("Your guess is below the secret number.")
elif guess > secret_number:
    print("Your guess is above the secret number.")
else:
    print("Congratulations! Your guess matches the secret number.")