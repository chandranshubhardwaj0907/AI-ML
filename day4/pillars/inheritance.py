# inheritance in python is a mechanism where a new class inherits properties and behaviors (attributes and methods) from an existing class. The existing class is called the "base" or "parent" class, and the new class is called the "derived" or "child" class. Inheritance promotes code reusability and establishes a hierarchical relationship between classes.

# resusing attr and methods of parent class in child class


class employee:
    start_time = "9 am"
    end_time = "6 pm"


class teacher(employee):  # teacher class is inheriting employee class
    def __init__(self, subject):
        self.subject = subject


t1 = teacher("maths")
print(t1.start_time)  # accessing parent class attribute
print(t1.subject)  # accessing child class attribute
print(teacher.end_time)  # accessing parent class attribute using child class

# types of inheritance
# 1) single inheritance
# 2) multilevel inheritance
# 3) hierarchical inheritance
# 4) multiple inheritance
# 5) hybrid inheritance


# 1) single inheritance -> when a child class inherits from a single parent class
class parent:
    def func1(self):
        print("this is function 1")


class child(parent):
    def func2(self):
        print("this is function 2")


c1 = child()
c1.func1()
c1.func2()


# 2) multilevel inheritance -> when a class inherits from a derived class, creating a multi-level hierarchy
class grandparent:
    def func1(self):
        print("this is function 1 from grandparent")


class parent(grandparent):
    def func2(self):
        print("this is function 2 from parent")


class child(parent):
    def func3(self):
        print("this is function 3 from child")


ch1 = child()
ch1.func1()
ch1.func2()
ch1.func3()


# 3) hierarchical inheritance -> when multiple child classes inherit from a single parent class
class parent:
    def func1(self):
        print("this is function 1 from parent")


class child1(parent):
    def func2(self):
        print("this is function 2 from child1")


class child2(parent):
    def func3(self):
        print("this is function 3 from child2")


ch1 = child1()
ch1.func1()
ch1.func2()
ch2 = child2()
ch2.func1()
ch2.func3()


# 4) multiple inheritance -> when a class inherits from more than one parent class
class parent1:
    def func1(self):
        print("this is function 1 from parent1")


class parent2:
    def func2(self):
        print("this is function 2 from parent2")


class child(parent1, parent2):
    def func3(self):
        print("this is function 3 from child")


ch1 = child()
ch1.func1()
ch1.func2()
ch1.func3()
