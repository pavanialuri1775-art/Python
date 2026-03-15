#6
#Even or odd
def is_even(num):
    if num%2==0:
        return True
    else:
        return False
num=int(input("enter a number:"))
print(is_even(num))

#7
#greet with default value
def greet(name="Pavani"):
    print(f"hello,{name}!")
greet()

#8
#Multiply three numbers
def multiply(a,b,c):
    return a*b*c
result=multiply(2,3,4)
print(result)

#9
#Area of a rectangle
def area_rectangle(a,b):
    return a*b
area=area_rectangle(4,8)
print(area)
    
#10
#Swap two numbers
def swap(a,b):
    return b,a
x,y=swap(3,10)
print(x,y)

