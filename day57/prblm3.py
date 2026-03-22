#5 Decorator should return the function output twice
def decorator(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)*2
    return wrapper
@decorator
def greet():
    return "Hi"
print(greet())

#6
def star(func):
    def wrapper():
        return "***"+func().upper()+"***"
    return wrapper
@star
def greet():
    return " Hello Pavani "
print(greet())
