#(Modify Outer Variable)
def outer():
    x=10
    def inner():
        nonlocal x
        x=100
    inner()
    print(x)
outer()

#
def outer():
    x=0
    def inner():
        nonlocal x
        x+=1
        print(x)
    return inner
counter=outer()
counter()
counter()
counter()

