##Add *** before and after output
def decorator(func):
    def wrapper(*args,**kwargs):
        return "***"+func()+"***"
    return wrapper
@decorator
def greet():
    return "hello pavani"
print(greet())

#add "result:" beofre output
def decorator(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        return "Result: "+str(result)
    return wrapper
@decorator
def add(a,b):
    return a+b
print(add(2,3))

#count how many times a function is called
def counter(func):
    count=0
    def wrapper(*args,**kwargs):
        nonlocal count
        count+=1
        print("called",count,"times")
        return func()
    return wrapper
@counter
def num():
    print("hello")
num()
num()
num()

#write a decorator works for any function and prints before execution and after execution
def decorator(func):
    def wrapper(*args,**kwargs):
        print("before execution")
        result=func(*args,**kwargs)
        print("after execution")
        return result
    return wrapper
@decorator
def add(a,b):
    print(a+b)
add(2,3)