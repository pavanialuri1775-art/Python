'''#1 Print numbers from 1 to n and store their sum in a variable
n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
   sum+=i
print("sum=",sum)'''

#2 Find the product of numbers from 1 to n
n=int(input("enter a number:"))
product=1
for i in range(1,n+1):
    product*=i
print(product)
