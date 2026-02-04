#tuple:Tuples are used to store multiple items in a single variable.
#Tuple items are ordered, immutable, and allow duplicate values.

'''mytuple = ("apple","banana","cherry")
print(mytuple)

#we use len() function to determine how many items a tuple has.
#Print the number of items in the tuple
thistuple = ("apple","banana","cherry")
print(len(thistuple)) #3

#Create Tuple With One Item
#To create a tuple with only one item,
#we have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple)) #<class 'tuple'>

#Tuple items can be of any data type and can contain different datatypes
tuple1 = ("abc",34,True,40,"male")
print(tuple1)  #('abc', 34, True, 40, 'male')'''

#The tuple() Constructor
#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)











