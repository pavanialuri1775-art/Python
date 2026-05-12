#
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        print("animal makes sound")
class child1(Animal):
    def dog(self):
        print("bow")
    def sound(self):
        print("dog is barking")
class child2(Animal):
    def cat(self):
        print("meow")
    def sound(self):
        print("cat says meow")
c1=child1()
c1.sound()
d1=child2()
d1.sound()
    