#real life example
def logger(func):
    def wrapper(*args, **kwargs):
        print("Function is running...")
        return func(*args, **kwargs)
    return wrapper
@logger
def add(a, b):
    return a + b
print(add(2, 3))

#Multiple Decorators
def star(func):
    def wrapper():
        return "*"+func()+"*"
    return wrapper
def hash(func):
    def wrapper():
        return "#"+func()+"#"
    return wrapper
@star
@hash
def greet():
    return "Hello"
print(greet())#*#Hello#*