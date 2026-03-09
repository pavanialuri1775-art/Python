'''#Print first 10 natural numbers using while loop
i=1
while i<=10:
    print(i)
    i+=1
    
#print the pattern 
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
   
#Calculate sum of all numbers from 1 to a given number
n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
    
#Print multiplication table of a given number
n=int(input("enter a number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)
    
#Display numbers from a list using a loop
numbers=[12,75,150,180,145,525]
for i in numbers:
   if i>500:
      break
   elif i>150:
      continue
   elif i%5==0:
      print(i)'''

#count the total number of digits in a 
#number using while loop
n=input("enter a number:")
count=0
while n!=0:
    n=int(n)//10
    count=count+1
print("total digits:",count)