#write a function that adds hello before function and welcome after function.
def decorator(greet):
    def wrap():
        print("Hello "+greet()+" Welcome")
    return wrap
@decorator
def greet():
    return "pavani"
greet()

#
def dec(func):
    def wrap(a,b):
        res=func(a,b)
        print(res*res)
    return wrap
@dec
def add(a,b):
    return a+b
@dec
def sub(a,b):
    return a-b
add(9,5)
sub(5,3)