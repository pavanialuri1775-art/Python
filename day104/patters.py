#1 triangle pattern
'''r=3
n=r-1
for i in range(r):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    print()
    
#2 reverse triangle
r=5
n=r-1
for i in range(r):
    for j in range(i):
        print(" ",end="")
    for k in range(2*r-1-2*i):
        print("*",end="")
    print()'''         
#reverse  triangle
r=3
n=r-1
for i in range(r-1,-1,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    print()
    
r=3
n=r-1
for i in range(r-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    print()
r=3
n=r-1
for i in range(r-1,-1,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    print()
    
#Regex ---------------------------------------------------

import re

text = input()# hi my email is bhavani.m@gmail.com
pattern = r"[\w.]+@[\w.]+\.\w+"
num = r"[\d+]+"

emails = re.findall(pattern, text)
n = re.findall(num, text)
print(emails, n)

