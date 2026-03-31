#1 global 
x=10
def show():
    print(x)
show()#10

#2 local 
def fun():
    x=5
    print(x)
fun()#5

#3 local vs global
x=2
def local_vs_global():
    x=5
    print(x)#5
local_vs_global()
print(x)#2

#4 modifying global using global keyword
x=10
def change():
    global x
    x=3
change()
print(x)#3

#5 print variable inside and outside function.
x=8
def function():
    print("inside function:",x)#8
function()
print("outside function:",x)#8

#6 same variable name inside & outside function
x=89
def name():
    x=85
    print("inside function:",x)#85
name()
print("outside function:",x)#89

#7 nested function accesing outer variable.
def outer():
    x=34
    def inner():
        print("inner function:",x)
    inner()#inner can access outer variable
outer()






