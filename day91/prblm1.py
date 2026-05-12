#1
class Employee:
    def __init__(self,name):
        self.name=name
class Developer(Employee):
    def __init__(self, name,prog_lang):
        super().__init__(name)
        self.lang=prog_lang
c1=Developer("pavani","python")
print(c1.name,c1.lang)

#2
class Animal:
    def wild(self):
        print("animal is shouting")
class pet(Animal):
    def dog(self):
        print("bow")
class sound(Animal):
    def cat(self):
        print("meow")    
d1=pet()   
d1.wild()    
d1.dog()       
d2=sound() 
d2.wild()  
d2.cat()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          