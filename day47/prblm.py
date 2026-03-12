#6 check palindrome
num=input("enter a number:")
i=0
j=len(num)-1
is_palindrome=True
while i<j:
    if num[i]!=num[j]:
        is_palindrome=False
        break
    i+=1
    j-=1
if is_palindrome:
    print("it is a palindrome")
else:
    print("not a palindrome")
    
#7 sum of digits of a nuber
num=int(input("enter a number:"))
total=0
while num>0:
    digit=num%10
    total=total+digit
    num=num//10
print(total)

#8 count how many digits in a number
num=int(input("enter a number:"))
count=0
while num>0:
    num=num//10
    count+=1
print(count)

#9  reverse a number
n=int(input("enter a number:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)

#10 Armstrong Number:sum of the cubes of its digits equals the number itself
num=int(input("enter a number:"))
total=0
original=num
while num>0:
    digit=num%10
    total=total+digit**3
    num=num//10
if total==original:
    print("Armstrong")
else:
    print("Not Armstrong")




    
 