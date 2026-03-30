#1
#function with default parameter
def greet(name="Pavani"):
    return f"Hello {name}"
print(greet())#Hello Pavani
print(greet("geetha"))

#2
#functions to multiply three numbers
def multiply(a,b,c):
    return a*b*c
print(multiply(2,3,4))#24

#3
#function using keyword arguments
def add(a,b,c):
    return a+b+c
print(add(a=5,b=6,c=3))#14

#4
#function to print name and age using kwargs
def function(**kwargs):
    return kwargs
result=function(name="Pavani",age=20)
print(result)#{'name': 'Pavani', 'age': 20} 

#5
#function that returns sum of 2 numbers with default values.
def add(a=10,b=20):
    return a+b
print(add())#30