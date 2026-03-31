#10 use nonlocal to increment variable in nested function.
def outer():
    x=20
    def inner():
        nonlocal x
        x+=1
        print(x)
    inner()
outer()
    
#11 compare local vs global in same program.
x=20
def outer():
    y=15
    def inner():
        global x
        nonlocal y
        x+=1
        y-=1
        print(x,y)#21,14
    inner()
    print(y)#14
outer()
print(x)#21  

#12 Demonstrate LEBG rule with 3variables.
x=10
def outer():
    z=15
    def inner():
        y=20
        print(y)
    inner()
    print(z)
outer()
print(x)
    






        
        
    