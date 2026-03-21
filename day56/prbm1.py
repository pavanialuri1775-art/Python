#decorator:A function that takes another function,adds extra behaviour and return the function.
#ex:
#starts with a normal function.
def greet():
    return "hello"
print(greet())#hello

#functions are "Objects" in python.
#functions behaves like a variables.
def greet():
    return "hello"
x=greet()
print(x)#hello

#nested function
def outer():
    def inner():
        print("inside inner function")#inside inner function
    inner()
outer()

#return a function
def outer():
    def inner():
        return "Hello from inner"
    return inner
f=outer()
print(f())#Hello from inner

#pass function as Argument
def greet():
    return "Hello"
def display(func):
    print(func())
display(greet)

#decorator concept:Add extra behavior to a function without changing it.
def greet():
    return "Hello"#without changing a  greet() code.
def decorator(func):
    def wrapper():
        return func().upper()
    return wrapper
greet=decorator(greet)
print(greet())#HELLO

#Shortcut → @ Syntax
#instead of writing greet=decorator(greet)
#we write
@decorator
def greet():
    return "Hello"


