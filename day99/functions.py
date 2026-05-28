#sum of 2 numbers
def add(a,b):
    return a+b
result=add(4,5)
print(result)

#even/odd
def even_or_odd(a):
    if a%2==0:
        print("even")
    else:
        print("odd")
result=even_or_odd(5)

#factorial
def factorial(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a
result=factorial(5)
print(result)

#
def largest_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
res=largest_num(54,3,32)
print(res)

        