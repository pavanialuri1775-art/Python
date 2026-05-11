#Method overriding
class Bird:
    def fly(self):
        print("birds are flying")
class penguin(Bird):
    def fly(self):
        print("i am flying")
s1=penguin()
s1.fly()

#
class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")
d = Dog()
d.sound()



