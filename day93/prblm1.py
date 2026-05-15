#1 overiding
class Animal:
    def sound(self):
        print("Animals makes sound")
class Dog(Animal):
    def sound(self):
        print("my dog name is charliee")
d1=Dog()
d1.sound()#my dog name is charliee

#2 
class Employee:
    def work(self):
        print("work done assigned by manager")
class Developer(Employee):
    def work(self):
        print('develops a project')
class Manager(Employee):
    def work(self):
        print("manages the work")
m1=Manager()
m1.work()#manages the work
d1=Developer()
d1.work()#develops a project

#3
class Payment:
    def pay(self,amount):
        self.amount=amount
        print(f"i have {self.amount} rupees")
class UPI(Payment):
    def pay(self,amount):
        self.amount=amount
        print(f"i pay {self.amount}rs through UPI")
class Card(Payment):
    def pay(self,amount):
        self.amount=amount
        print(f"i pay {self.amount}rs through card")
c1=Card()
c1.pay(25000)#i pay 25000rs through card
u1=UPI()
u1.pay(30000)#i pay 30000rs through UPI
d1=Payment()
d1.pay("45000")#i have 45000 rupees
