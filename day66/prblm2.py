#8 nonlocal keyword
def outer():
    x=10
    def inner():
        nonlocal x
        x=20
    inner()
    print(x)
outer()#20

#9 LEGB rule
x="global"
def outer():
    x="enclosing"
    def inner():
        x="local"
        print(x)#local
    inner()
    print(x)#enclosing
outer()
print(x)#global


