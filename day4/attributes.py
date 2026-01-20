class student:
    college_name = "Thapar"
    PI = 3.1
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.PI = 3.14  # instance attribute
        
s1 = student("Alice", 20)
s2 = student("Bob", 22)

print("College Name (class attribute):", student.college_name)
print("PI from class (class attribute):", student.PI)
print("PI from instance (instance attribute):", s1.PI)

print(s1.PI)  # Accessing instance attribute