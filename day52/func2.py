#Postional-only Arguments
def greet(name,/):
    print("Hello",name)
greet("Pavani")

#keyword only Argument
def show_age(*,age):
    print("Age is",age)
show_age(age=21)

#
def calculate(a,b,/,*,c,d):
    print(a+b+c+d)
calculate(2,3,c=4,d=5)#14
    
    