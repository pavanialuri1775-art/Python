#Divide Two Numbe
a,b=map(int,input().split())
try:
    print(a/b)
except ZeroDivisionError:
    print("cannot divide by zero")
    
#Integer Input Validation
try:
    n=int(input())
    print("valid")
except:
    print("Invalid")
    
    

        