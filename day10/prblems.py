#Initialize a variable x = 10 and increase it by 5 using assignment operator.
x=10
x+=5
print(x)

#Check if a number is greater than 0 AND less than 100.
x=23
if x>0 and x<100:
    print("the num is between the range")
else:
    print("the num is not in the range")
    
#check if a number is divisible by 2 0r divisible by 3
x=int(input("enter a number:"))
if x%2==0 or x%3==0:
      print("x is divisible by 2 or 3")
else:
    print("x is not divisble by 2 0r 3")
    
#check if a character is a vowel using logical operators
ch=input("enter a character:")
if ch=="a" or ch=="e" or ch=="i" or ch =="0" or ch=="u":
    print("it is a vowel")
else:
    print("not a vowel")
    
#Take 3 numbers and find the largest using comparison operators
a=2
b=5
c=8
if a>b and a>c:
    print("a is the largest number")
elif b>a and b>c:
    print("b is the largest number")
else:
    print("c is the largest number")
 # Take two numbers and print True if both are equal and even
a=4
b=4
if a==b and a%2==0:
    print(True)
    
#Check if a number is power of 2 using bitwise operator.
n=int(input("enter a number:"))
if n>0 and (n&(n-1))==0:
    print("yes,it is a power of 2")
else:
    print("no")
    
#Take two numbers and print True if one is a factor of the other.
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if a%b==0 or b%a==0:
    print("True")
else:
    print("False")




