#with arguments
def decorator(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper
@decorator
def greet(name):
    return "Hello "+name
print(greet("Pavani"))

#if function has many arguments
def decorator(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return wrapper
@decorator
def my_fun(name,city):
    return "Hello i am "+name+" i live in "+city
print(my_fun("pavani","hyderabad"))#HELLO I AM PAVANI I LIVE IN HYDERABAD


