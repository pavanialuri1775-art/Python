'''#print numbers from i to N
n=int(input("enter a number:"))
for i in range(1,n+1):
    print(i)
    
    
#print all even numbers from 1 to N
n=int(input("enter a number:"))
for i in range(1,n+1):
    if i%2==0:
        print(i)
        
#sum of first N numbers
n=int(input("enter a number:"))#10
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)#55'''

#count digits in a number
n=input("Enter a number:")#78945
count=0
for digit in n:
    count+=1
print(count)#5