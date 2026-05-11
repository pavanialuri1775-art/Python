#Multilevel Inheritance
class Person:
    def show_name(self,name):
        self.name=name
        print("my name is",self.name)
class Employee(Person):
    def show_salary(self,salary):
        self.salary=salary
        print("my salary is",self.salary)
class Manager(Employee):
    def show_department(self,department):
        self.department=department
        print("she belongs to",self.department,"department")
m1=Manager()
m1.show_name("pavani")
m1.show_salary(20000)
m1.show_department("AIML")

#
class Person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print(self.name)
class Employee(Person):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary=salary
    def show_salary(self):
        print(self.salary)
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name, salary)
        self.department = department
    def show_department(self):
        print(self.department)
    
m1 = Manager("Pavani", 50000, "AI")
m1.show_name()
m1.show_salary()
m1.show_department()
        