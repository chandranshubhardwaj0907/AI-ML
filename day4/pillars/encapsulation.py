
# Encapsulation
# wrapping data and functions into a single unit

# data hiding --> hiding private information

# we have 3 types of attributes

# 1) public -> attributes can be accessed
# inside and outside the class
# 2) protected -> can be accessed inside the class and its subclasses
# 3) private -> attributes can be accesed only inside the class only


class bankaccount:
    def __init__(self, name, balance, accountnumber):
        self.name = name  # public attribute
        self._balance = balance  # protected attribute just add single underscore
        self.__accountnumber = accountnumber  # private attribute

    def get_accountnumber(self):  # getter method to access private attribute
        return self.__accountnumber

    def set_accountnumber(self, new_accountnumber):  # setter method to modify private attribute
        self.__accountnumber = new_accountnumber
        
acc1 = bankaccount("john", 5000, "12345")
print(acc1.name)  # accessing public attribute
print(acc1._balance)  # accessing protected attribute
print(acc1.get_accountnumber())  # accessing private attribute
