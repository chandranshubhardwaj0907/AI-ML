# __init__Method


class student:
    def __init__(self, name, cgpa):

        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stu1 = student("RAHUL", 9.0)
stu2 = student("Chandu", 9.80)

print(stu1.name, stu1.cgpa)
print(stu2.name, stu2.cgpa)

print(stu1.get_cgpa())

#  TYPES OF CONSTRUCTOR

# 1-> default -- which has only self parameter
# 2-> parameterized -- which has different parameters