#inverted right angle triangle
'''for i in range(5,0,-1):
    print("*"*i)
    
#same number pattern
n=5
for i in range(1,n+1):
    print(str(i)*i)'''
    
#using nested for loop
n=5
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()