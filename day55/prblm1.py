#6
def my_function():
    x=10
    def my_func():
        nonlocal x
        x=50
    my_func()
    print(x)
my_function()

#7
def outer():
    count=0
    def inner():
        nonlocal count
        count+=1
    inner()
    inner()
    inner()
    print(count)
outer()

#8
count=0
def my_fun():
    global count
    count+=1
my_fun()
my_fun()
my_fun()
print(count)

#9
x="global"
def my_fun():
    x="outer"
    def my_func():
        print(x)#outer
    my_func()
my_fun()

#10
def my_fun():
    x=10
    def my_func():
        print(x)
    x=20
    my_func()
my_fun()

    
    