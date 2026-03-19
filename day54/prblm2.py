#1
def my_fun():
    x=10
    print(x)#10
my_fun()

#2
x=50
def my_fun():
    print(x)
my_fun()

#3
x=100
def my_fun():
    x=20
    print(x)
my_fun()
print(x)

#4
x=10
def my_fun():
    global x
    x=99
my_fun()
print(x)
    
#5
def my_fun():
    x=5
    def my_func():
        print(x)
    my_func()
my_fun()
