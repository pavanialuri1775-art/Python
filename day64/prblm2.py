#6Factorial of a number
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
print(factorial(5))#120

#7 Factorial of a number(recursion)
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))#120

#8 Fibonacci using functionm
def fibonacci(n):
    a,b=0,1
    result=[]
    for i in range(n):
        result.append(a)
        a,b=b,a+b 
    return result
print(fibonacci(5))

#9 fibonacci number(using recursion)
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(4))#3

#10 Check palindrome
def is_palindrome(s):
    return s==s[::-1]
print(is_palindrome("12321"))

#11
def is_palindrome(s):
    rev=""
    for ch in s:
        rev=ch+rev
    return s==rev
print(is_palindrome("madam"))#True

#12 using recursion
def is_palindrome(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("madam"))#True
        
    
    
    

