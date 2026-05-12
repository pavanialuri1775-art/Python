#
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):                                                
        print("surface of a shape is Area")
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length *self.width
s1=Circle(5)
r=Rectangle(4,6)
print(s1.area())
print(r.area())

#
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print("vehicle is started")
class Child1(Vehicle):
    def car(self):
        print("car is 4-wheeler vehicle")
    def start(self):
        print("car is in red color")
class Bike(Vehicle):
    def bike(self):
        print("it is 2-wheeler")
    def start(self):
        print("it is in blue color")
c1=Child1()
c1.car()
c1.start()