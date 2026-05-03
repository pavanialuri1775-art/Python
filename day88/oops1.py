#super() Function
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)   
        self.age=year
    def Welcome(self):
        print("Welcome",self.firstname,self.lastname,"of age",self.age,"to the class")
s1=Student("pavss","aluri",21)
s1.Welcome()
s1.printname()