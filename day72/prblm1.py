#fibonacci series
def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
fibonacci(5)

#fibonacci series using recursion
def fibonacci_R(n):
    if n<=1:
        return n
    return fibonacci_R(n-1)+fibonacci_R(n-2)
n=6
for i in range(n):
    print(fibonacci_R(i),end=" ")
    
#inversion of dictionary
d={"a":1,"b":2}
for key,value in d.items():
    print(f"{value}:{key}")
    
#
def wave(s):
    n=len(s)
    for i in range(n):
        print(" "*i+s[i])
        for i in range(n,0,-1):
            print(" "*i+s[i])
wave(list("CODE"))
        