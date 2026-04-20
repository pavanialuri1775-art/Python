# 4
try:
    n=int(input("enter a number:"))
    b=int(input("enter a number"))
    print(n/b)
except ValueError:
    print("Ivalid input")
except ZeroDivisionError:
    print("cannot divide by zero")
    
#5
try:
    a=int(input("enter a num:"))
    b=int(input("enter a num:"))
    c=a+b
except ValueError:
    print("Invalid input")
else:
    print(c)
    print("addition succesful") 
    
#   
try:
    n=int(input("enter a number:"))
except ValueError:
    print("invalid input") 
finally:
    print("program ended")                            