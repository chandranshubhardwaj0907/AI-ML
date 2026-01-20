from day4.pillars.encapsulation import bankaccount

# Q1. Create a class BankAccount with attributes account_number, owner_name,
# and balance.
# Add methods to deposit, withdraw, and check balance


class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")

    def check_balance(self):
        return self.balance


acc1 = BankAccount("123456789", "Alice", 1000)
acc1.deposit(500)
acc1.withdraw(200)
print(f"Current balance is {acc1.check_balance()}")
