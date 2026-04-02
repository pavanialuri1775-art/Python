# Print numbers 1 to n
def numbers(n):
    if n==0:
        return
    numbers(n-1)
    print(n)
numbers(5)

#Print n to 1
def numbers_ex(n):
    if n==0:
        return
    print(n)
    numbers_ex(n-1)
numbers_ex(5)

#Factorial 
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)
print(factorial(5))