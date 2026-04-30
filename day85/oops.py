#OOp=Object-Oriented Programming.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("pavani",21)
print(p1.name)
print(p1.age)

#Without the __init__() method, you would need to set properties manually for each object.
class Person:
      pass
p1 = Person()
p1.name = "Tobias"
p1.age = 25
print(p1.name)
print(p1.age)

#Default Values in __init__()
class Person:
    def __init__(self,name,age=21):
        self.name=name
        self.age=age
p1=Person("Emil")
p2=Person("Pavss",21)
print(p1.name,p1.age)
print(p2.name,p2.age)

#Multiple Parameters
#The __init__() method can have as many parameters as you need.
class person:
    def __init__(self,name,age,city,gender):
        self.name=name
        self.age=age
        self.city=city
        self.gender=gender
p1=person("pavss",20,"hyd","female")
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.gender)
        
