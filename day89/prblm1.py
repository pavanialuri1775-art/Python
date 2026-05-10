#prblm1
#basic inheritance
'''class Vehicle:
    def start(self):
        print("vehicle started")
class Car(Vehicle):
    def stop(self):
        print("vehicle stopped")
s1=Car()
s1.start()'''

#prblm2
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self, name, age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no
x=Student("Pavss","21",6609)
def welcome(self):
    print("I am",self.name,"of age",self.age,"with the roll_no",self.roll_no,"studying at GNIT")