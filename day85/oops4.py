#Class Properties vs Object Properties
#Properties defined inside __init__() belong to each object.
#Properties defined outside methods belong to the class itself (class properties) and are shared by all objects.
#Class property vs instance property.
class Person:
    species="Human"
    def __init__(self,name):
        self.name=name
p1=Person("pavani")
p2=Person("pavss")
print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

#Modifying Class Properties.
#When we modify a class property it affects all objects.
class Person:
    lastname=""
    def __init__(self,name):
        self.name=name
p1=Person("pavss")
p2=Person("pavnii")
Person.lastname="Aluri"
print(p1.lastname)
print(p2.lastname)

#Add new properties:Add a new property to an object
class Person:
      def __init__(self, name):
         self.name = name
p1=Person("Pavani")
p1.age=21
p1.city="oslo"
print(p1.name)
print(p1.age)
print(p1.city)
#Adding properties this way only adds them to that specific object, not to all objects of the class.
