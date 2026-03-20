#1
def my_func():
    x=25
    print(x)#25
my_func()

#2(global usage)
x=100
def my_fun():
    print(x)#100
my_fun()

#3((Modify Global)
x=10
def my_fun():
    global  x
    x=50
my_fun()
print(x)#50

#4(Local vs Global)
x=99
def my_fun():
    x=1
    print(x)#1
my_fun()
print(x)#99

#5(nested function)
def outer():
    x=7
    def inner():
        print(x)
    inner()
outer()
    