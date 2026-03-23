#multiply result
def dec(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)*2
    return wrapper
@dec
def multiply():
    return 5
print(multiply())

#adding result before output
def dec(func):
    def wrapper(*args,**kwargs):
        return "result: "+str(func(*args,**kwargs)*2)
    return wrapper
@dec
def multiply():
    return 5
print(multiply())



