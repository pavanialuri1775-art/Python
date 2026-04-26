#SQUARE PATTERN
n=int(input("enter a number:"))
for i in range(n):
    print("*"*n)
    
#right angle triangle
n=int(input("enter a number:"))
for i in range(1,n+1):
    print("*"*i)
    
#inverted traingle
n=int(input("enter a number:"))
for i in range(n,0,-1):
    print("*"*i)
    
#pyramid traingle
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()