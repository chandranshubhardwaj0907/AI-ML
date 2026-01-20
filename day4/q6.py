# Q6. Create an abstract class with an abstract method , calculate_salary(). 
# Create subclasses ,  and that 
# implement the method differently.

from abc import ABC, abstractmethod

class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    
class FullTimeEmployee(employee):
    def calculate_salary(self):
        return 50000

class PartTimeEmployee(employee):
    def calculate_salary(self):
        return 25000

class Contractor(employee):
    def calculate_salary(self):
        return 30000
    
# Objects
fte = FullTimeEmployee()
pte = PartTimeEmployee()
contractor = Contractor()
print("Full Time Employee Salary:", fte.calculate_salary())
print("Part Time Employee Salary:", pte.calculate_salary())
print("Contractor Salary:", contractor.calculate_salary())