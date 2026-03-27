#recursion:A function calling itself
#every recursion must have
#1.Base case(stopping condition)
#2.Recursion Case(function calls itself)
#ex:countdown
def countdown(n):
    if n<=0:
        print("Done!")
    else:
        print(n)
        countdown(n-1)
countdown(5)

#ex2
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
