#Returning different data types
def my_function():
    return ["apple", "banana", "cherry"]
fruits=my_function()
print(fruits[0])
print(fruits[2])

#functions that returns a tuple
def my_function():
    return (10,20)
x,y=my_function()
print(x)
print(y)

#Positional-Only Arguments
#To specify positional-only arguments, add , / after the arguments
def my_function(name,/):
    print("hello",name)
my_function("pavani")

#Keyword-Only Arguments
#To specify that a function can have only keyword arguments, add *, before the arguments
def my_function(*, name):
      print("Hello", name)
my_function(name = "Emil")

#Combining Positional-Only and Keyword-Only
def add(a,b,/,*,c,d):
    return a+b+c+d
result=add(2,3,c=5,d=6)
print(result)