#The self Parameter
#The self parameter is a reference to the current instance of the class.
#It is used to access properties and methods that belong to the class.
class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age
      def greet(self):
          print("hello,my name is "+self.name)
p1=Person("pavss",20)
p1.greet()

#self Does Not Have to Be Named "self"
#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class.
#Use the words myobject and abc instead of self.
class Person:
      def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age
      def greet(abc):
        print("Hello, my name is " + abc.name)
p1 = Person("Emil", 36)
p1.greet()

#Accessing Properties with self
class Car:
      def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
      def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")
car1=Car("toyota","corolla",2020)
car1.display_info()

#Calling Methods with self
#You can also call other methods within the class using self
class Person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        return "hello, "+self.name
    def Welcome(self):
        message=self.greet()
        print(message+ "! Welcome to oue website.")
p1=Person("pavani")
p1.Welcome()

