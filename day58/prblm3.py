#decoration with argument
def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                print(func(*args,**kwargs))
        return wrapper
    return decorator
@repeat(3)
def greet():
    return "hello"
greet()