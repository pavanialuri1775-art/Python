#Class Methods
#Methods are functions that belong to a class.
#They define the behavior of objects created from the class.
#create a method in class.
class Person:
      def __init__(self, name):
        self.name = name
      def greet(self):
         print("Hello, my name is " + self.name)
p1 = Person("Emil")
p1.greet()

#All methods must have self as the first parameter.
#Methods with Parameters:Methods can accept parameters just like regular functions.
#Create a method with parameters
class Calculator:
      def add(self, a, b):
        return a + b
      def multiply(self, a, b):
        return a * b
calc=Calculator()
print(calc.add(5,3))
print(calc.multiply(2,3))

#Methods Accessing Properties
#Methods can access and modify object properties using self.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_info(self):
        return f'{self.name} is {self.age} years old'
p1=Person("pavani",21)
print(p1.get_info())

#Methods can modify properties
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def cel_birthday(self):
        self.age+=1
        print(f"Happy Birthday! you are now {self.age}")
p1=Person("pavss",21)
p1.cel_birthday()#22
p1.cel_birthday()#23




        