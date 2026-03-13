#1 Pattern Printing with While Loop  
n=int(input("enter a number:"))
i=1
while i<=n:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    print()
    i+=1
    
#2 inverted triangle 
n=int(input("enter a number:"))
i=n
while i>=1:
    j=i
    while j>=1:
        print("*",end="")
        j-=1
    print()
    i-=1
    
#3 sum of even digits
n=int(input("enter a number:"))
sum=0
while n>0:
    digit=n%10 #extracts last digit
    if digit%2==0:
        sum=sum+digit
    n=n//10
print(sum)

#4 sum of odd digits
n=int(input("enter a number:"))
sum=0
while n>0:
    digit=n%10 #extracts last digit
    if digit%2==1:
        sum=sum+digit
    n=n//10
print(sum)