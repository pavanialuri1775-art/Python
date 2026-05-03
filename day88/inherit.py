#Python Inheritance
#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.
#Create a Parent Class
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
x=Person("Pavani","aluri")
x.printname()

#Create a Child class  
class student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
s1=student("pavss","puppie")
print(s1.firstname)
print(s1.lastname)



 
        
        