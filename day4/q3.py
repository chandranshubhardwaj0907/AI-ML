class Student:
    def __init__(self):
        self.__name = ""
        self.__roll_no = 0
        self.__marks = 0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("Name cannot be empty.")

    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100.")

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Marks cannot be negative.")


s = Student()

s.set_name("Alice")
s.set_roll_no(25)
s.set_marks(85)

print("Name:", s.get_name())
print("Roll No:", s.get_roll_no())
print("Marks:", s.get_marks())
