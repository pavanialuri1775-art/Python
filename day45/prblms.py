#fibonacci series using functions
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c
n=int(input("enter a number:"))
fibonacci(n)

#arithmetic operations
def operations():
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)
    print(a//b)
operations()
