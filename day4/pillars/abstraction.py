# in data hiding we hide private information
# abstraction is showing only essential things to the user

# abstract class means its just a blueprint which help to make a blueprint for the other class

from abc import ABC, abstractmethod


class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class lion(animal):
    def make_sound(self):
        print("roar")


class dog(animal):
    def make_sound(self):
        print("bark")
        
lion = lion()
lion.make_sound()
dog = dog()
dog.make_sound()
        
