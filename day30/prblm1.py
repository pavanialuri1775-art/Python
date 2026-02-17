#checking even or odd
num=int(input("enter a number:"))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")
    
#shorthand if else:it is a easy way to write an if-else condition in one line.
a=27
b=30
print("a is greater")if a>b else print("b is greater")

#checking even or odd using shorthand if else
num=int(input("enter a number:"))
print("number is even")if num%2==0 else print("number is odd")