#1
#Create a decorator that adds "Hello " before the function output.
def dec(fun):
    def wrapper():
        return "Hello "+fun()+" Welcome"
    return wrapper
@dec
def greet():
    return "Pavani"
print(greet())

#2
def dec(func):
    def wrapper():
        return func().upper()+"!!!"
    return wrapper
@dec
def greet():
    return "hello pavani"
print(greet())
        