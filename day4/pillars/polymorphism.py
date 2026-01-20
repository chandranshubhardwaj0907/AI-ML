#  poly means many and morphism means forms
#  polymorphism means many forms


# functionn overriding
class bird:
    def fly(self):
        print("bird is flying")
        
class airplane:
    def fly(self):
        print("airplane is flying")
        
b1 = bird()
b1.fly()

# DUCK TYPING

class dog:
    def sound(self):
        print("bark")
        
class cat:
    def sound(self):
        print("meow")
        
        
c1 = cat()
c1.sound()