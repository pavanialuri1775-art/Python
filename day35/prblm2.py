#Factorial of a number
'''n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

#reverse of a number
n=input("enter a number:")#12345
rev=""
for ch in n:
    rev=ch+rev
print(rev)#54321'''

#sum of digits
n=input("Enter a number:")
sum=0
for ch in n:
    sum+=int(ch)
print(sum)