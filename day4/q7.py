# Create a class that allows the constructor to work with: 
# •  name only 
# •  name + age 
# •  name + age + address 
# As direct constructor overloading (multiple constructors) are not allowed but 
# we have to use default parameters to simulate constructor overloading

class person:
    def __init__(self , name , age  = None , address = None):
        self.name = name
        self.age = age
        self.address = address
        
    def display(self):
        print("name:", self.name)
        if self.age is not None:
            print("age:", self.age)
        if self.address is not None:
            print("address:", self.address)
            
p1 = person("ALICE" ,25)
print(person.display(p1))