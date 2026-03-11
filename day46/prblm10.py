#4 Number patterns
'''n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
#1
#12
#123
#1234
#12345

#5 reverse pattern
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print(j,end="")
    print()
#54321
#4321
#321
#21
#1   

#6 same number pattern
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()
#1
#22
#333
#4444
#55555'''

#pattern 7
n=int(input("enter a number:"))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end="")
        num+=1
    print()
    
    
