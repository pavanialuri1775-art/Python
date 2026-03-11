#alphabet pattern
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end="")
    print()
    
#repeating character
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(i):
        print(chr(64+i),end="")
    print()
