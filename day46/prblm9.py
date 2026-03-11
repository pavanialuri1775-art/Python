#pattern1
'''n=int(input("enter a number:"))
for i in range(1,n+1):         
    for j in range(i):         
        print("*",end="")      
    print() 
#*
#**
#***
#****
#*****    

#pattern2
n=int(input("enter a number:"))             
for i in range(1,n+1):
    for j in range(n+1-i):
        print("*",end="")
    print()
#*****
#****
#***
#**
#*'''

#pattern3
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end="")
    print()