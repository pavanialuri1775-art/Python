#idetity operators:Identity operators are used to compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location

#is:Returns True if both variables are the same object
#The is operator returns True if both variables point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#The is not operator returns True if both variables do not point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#Difference Between is and ==
#is - Checks if both variables point to the same object in memory
#== - Checks if the values of both variables are equal
#example
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)