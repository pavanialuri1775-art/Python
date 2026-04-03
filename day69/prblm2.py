#fibonacci series
def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
fibonacci(5)

#using generator
def fibonacci_gen(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
for num in fibonacci_gen(7):
    print(num,end=" ")
    
#using recursion
def fibonacci_rec(n):
    if n<=1:
        return n
    return fibonacci_rec(n-1)+fibonacci_rec(n-2)
n=6
for i in range(n):
    print(fibonacci_rec(i),end=" ")
    
#
def fibonacci_num(n):
    if n<=1:
        return n
    return fibonacci_num(n-1)+fibonacci_num(n-2)
print(fibonacci_num(6))
    