#3Create a decorator that reverses a string and convert to uppercase
def decorator(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)[::-1].upper()
    return wrapper
@decorator
def greet():
    return "hello pavani"
print(greet())#INAVAP OLLEH

#4
def decorator(func):
    def wrapper(*args,**kwargs):
        print("Function started")
        result=func(*args,**kwargs)
        print(result)
        print("Function ended")
        return result
    return wrapper
@decorator
def greet():
    return "Hello Pavani"
print(greet())
