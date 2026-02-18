#checking if a year is a leapyear
'''num=int(input("Enter a number:"))
if num%4==0 and num%100!=0 or num%400==0:
    print("leap year")
else:
    print("not a leap year")
    
#Traingle type checker
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a==b and a==c:
    print("Equilateral triangle")
elif a==b or a==c:
    print("Isosceles triangle")
else:
    print("Scalene")
    
#How to Check Username and Password
crt_username="pavani"
crt_password=12345
username=input("Enter username:")
password=int(input("enter a password:"))
if username==crt_username and password==crt_password:
    print("Login Successful")
elif username==crt_username and password!=crt_password:
    print("Wrong password")
elif username!=crt_username and password==crt_password:
    print("Wrong username")
else:
    print("invalid login")
    
# check whether a character is Vowel or Consonant
a=input("Enter a character:")
vowels="aeiouAEIOU"
if a in vowels:
    print("vowel")
else:
    print("consonant")
    
#Take 3 angles and check if they form a valid triangle.
angle1=int(input("Enter an angle:"))
angle2=int(input("Enter an angle:"))
angle3=int(input("Enter an angle:"))
sum=angle1+angle2+angle3
if sum==180:
    print("valid triangle")
else:
    print("invalid")
    
#Check whether a number is divisible by 5 or not.
num=int(input("enter a number:"))
if num%5==0:
    print("yes it is divisible")
else:
    print("no")'''
    
#Grading system
marks=int(input("enter marks:"))
if marks>=90:
    print("A grade")
elif marks>=75:
    print("B grade")
elif marks>=60:
    print("C grade")
else:
    print("Fail")
    





    
    




    
