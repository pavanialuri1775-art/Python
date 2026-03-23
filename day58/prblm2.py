#counting how many times a function is called.
def counter(func):
    def wrapper(*args,**kwargs):
        wrapper.count+=1
        print(f"called {wrapper.count} times")
        return func(*args,**kwargs)
    wrapper.count=0
    return wrapper
@counter
def greet():
    print("hello")
greet()
greet()
greet()