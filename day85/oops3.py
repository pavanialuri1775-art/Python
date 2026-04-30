#Class Properties
#Properties are variables that belong to a class. They store data for each object created from the class.
#Create a class with properties.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("pavss",20)
print(p1.name)
print(p1.age)

#we can access properties of an object using the dot notation.
class Car:
      def __init__(self, brand, model):
        self.brand = brand
        self.model = model
car1 = Car("Toyota", "Corolla")
print(car1.brand)#toyota
print(car1.model)#corolla

#Modify properties
#we  can modify the value of properties on objects.
class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age
p1=Person('pavss',20)
print(p1.age)#20
p1.age=21
print(p1.age)#21

#delete Properties
#we can delete properties from objects using the del keyword
class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age
p1=Person("pavss",21)
del p1.age
print(p1.name)#pavss




    