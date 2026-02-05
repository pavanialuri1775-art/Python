#packing a Tuple
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple.
'''fruits = ("apple", "banana", "cherry")
print(fruits)

# Unpacking: we can extract values by assigning tuple elements to seperate variables.
#example:Unpacking a tuple
t=(10,20,30)
a, b,c =t
print(a)
print(b)
print(c)

#Number of variables must match number of tuple elements.

#Unpacking with Different Data Types
data=("apple",5,2.5)
fruit, quantity, price = data
print(fruit)
print(quantity)
print(price)'''

#
numbers = (1, 2, 3, 4, 5)
a,*b = numbers
print(a)   # 1
print(b)   # [2, 3, 4, 5]













