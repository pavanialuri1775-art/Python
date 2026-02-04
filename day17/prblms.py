#Average of 3 Numbers
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
a+=b
a+=c
a/=3
print(a)

#Check Range
n=int(input("Enter a number:"))
print(n>10 and n<50)

#Check Not Equal
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
print(x!=y) #True

#Both Even Check
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
print(x%2==0 and y%2==0)

#At Least One Condition True
age=16
has_id=True
print((age>18) or has_id)

#Check Even/Odd Using Bitwise
n=int(input("enter a number:"))
if n&1==1:
    print("odd")
else:
    print("even")
    
#without if else
n=int(input("enter a number:"))
print((n&1==0))

#Multiply by 8 Using Left Shift
num=int(input("enter a number:"))
print(num<<8)

#Divide by 4 Using Right Shift
num =int(input("enter a number:"))
print(num>>4)






