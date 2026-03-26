#converting given string to lower case
def decorator(func):
    def wrapper(*args,**kwargs):
        return func().lower()
    return wrapper
@decorator
def greet():
    return "HELLO PAVANI"
print(greet())

#
def square(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)**2
    return wrapper
@square
def multiply(a,b):
    return a*b
print(multiply(2,3))


