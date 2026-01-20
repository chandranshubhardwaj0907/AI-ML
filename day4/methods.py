# instance --> we have to write self in the parameters of the method

class Circle:
    def __init__(self , radius):
        self.radius = radius 


    def area(self):
        return 3.14 * self.radius * self.radius
        
  
L1 = Circle(5)
print(L1.area())  # Calling the method using the instance  

# class --> we have to write class name in the parameters of the method

class MathOperations:
    @classmethod
    def add(cls, a, b):
        return a + b
opr1 = MathOperations()
print(opr1.add(3, 4))  # Calling the class method using the instance

# static --> we don't have to write anything in the parameters of the method
class Utility:
    @staticmethod
    def multiply(a, b):
        return a * b
    
util1 = Utility()
print(util1.multiply(3, 4))  # Calling the static method using the instance