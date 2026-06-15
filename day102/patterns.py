#patters
#right angled pattern
'''for i in range(1,5):
    print(i*"*")
    
#using nested loop
for i in range(1,5):
    for j in range(i):
        print("*",end="")
    print()
    
#reverse right angled triangle
for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print()
    
#number pattern
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()'''

#same number pattern
for i in range(1,5):
    for j in range(i,i+1):
        print(j*j,end="")
    print()