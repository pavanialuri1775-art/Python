#variable
#it is a name given to a memory location to store data.
#ex:
x=10
name="Pavani"

#problem
name="Pavani"
age=21
marks=85
print("name:",name)
print("age:",age)
print("age:",age)

'''Python is dynamically typed because we do not need to declare the data type in advance, python 
automatically decides at the run time'''

x = 10
print(type(x))  

x = 10.5
print(type(x))   

x = "Python"
print(type(x))   

#python builtin  data types
#python has mutable and immutable datatypes.
#mutable:can change value after creation
#Immutable:cannot change value after creation.
#int
#float
#str
#boolean
#complex
#list
#tuple
#range
#dictionary
#none

#int(whole numbers either positive or negative)
a = 10
b = -5
print(a, b)
#float(decimal values)
marks=5.1
price=22.3
print(marks,price)
#string(text data enclosed in  quotes)
name='pavani'
course="b.tech"
#boolean(true/false)
is_student=True
is_passed=False
#**used in decison making
#
#none type(represents no value)
x=None
print(x)
#Multiple variable assignment
a = b = c = 10
#multiple value assignment
x, y, z = 1, 2, 3
print(x, y, z)
#complex
a = 3 + 4j
print(a)
print(type(a))

#list(square brackets)
#A list is a built-in data type in Python used to store multiple values in a single variable.

'''Key Features of List:
>Ordered
>Mutable (can be changed)
>Allows duplicate values
>Can store different data types'''
#example:
data = [10, 3.5, "Python", True]
print(data)

#tuple(same as list but enclosed with paranthesis)
##ordered
#immutable
#ex
t=(1,2,3)

#set
#unordered
#no duplicates
s={1,2,3,3}
print(s)

#dictonary 
#stores data as key-value pairs
student={"name":"Pavani",
         "age" : 20
         }














