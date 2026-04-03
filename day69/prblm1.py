#factorial of a number
def factorial_rec(n):
    if n<=1:
        return n
    return n*factorial_rec(n-1)
print(factorial_rec(5))

#
def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
print(factorial(5))

#
def sum_of_num(n):
    total=0
    for i in n:
        total+=int(i)
    return total
print(sum_of_num("1234"))

#
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(is_prime(7))

#largest of 3numbers
def largest_num(a,b,c):
    return max(a,b,c)
print(largest_num(23,45,12))#45

#reversing a string
def rev_string(s):
    rev=""
    for ch in s:
        rev=ch+rev
    return rev
print(rev_string("pavani"))#inavap

#to check if a  string is a palindrome
def palindrome(s):
    if s==s[::-1]:
        return True
    return False
print(palindrome("pavani"))
    
        