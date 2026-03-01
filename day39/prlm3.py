#count even and odd numbers in a string
n=input("enter a number:")
evencount=0
oddcount=0
for i in n:
    if int(i)%2==0:
        evencount+=1
    else:
        oddcount+=1
print(evencount)
print(oddcount)