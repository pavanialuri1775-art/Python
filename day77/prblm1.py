#print 1 to n numbers using functions
def numbers(n):
    for i in range(1,n+1):
        print(i)
s=int(input())
numbers(s)

#reverse a string using functions --str = "Hello"
def rev_fun(s):
    rev=""
    for ch in s:
        rev=ch+rev
    return rev
r=input()
print(rev_fun(r)

#
def rev_fun(s):
    return s[::-1]
r=input()
print(rev_fun(r))