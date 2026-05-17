#problem 1
class Animal:
    def sound(self):
        print("Animals makes sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
        
D1=Dog()
D1.sound()
C1=Cat()
C1.sound()

#problem2
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def calculate_salary(self):
        return self.salary
class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus=bonus
    def calculate_salary(self):
        return self.salary+self.bonus
class Developer(Employee):
    def __init__(self,name,salary,allowance):
        super().__init__(name,salary)
        self.allowance=allowance
    def calculate_salary(self):
        return self.salary+self.allowance
class Intern(Employee):
    def __init__(self,name,salary,stipend):
        super().__init__(name,salary)
        self.stipend=stipend
    def calculate_salary(self):
        return self.salary+self.stipend
M=Manager("pavnii",50000,10000)
D=Developer("geetha",40000,5000)
I=Intern("keerti",30000,5000)
print(f"{M.name}'s salary is {M.calculate_salary()}")
print(f"{D.name}'s salary is {D.calculate_salary()}")
print(f"{I.name}'s salary is {I.calculate_salary()}")