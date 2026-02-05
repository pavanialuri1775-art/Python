#Once a tuple is created, we cannot change its values. Tuples are unchangeable, or immutable.
#But we can convert the tuple into a list, change the list, and convert the list back into a tuple.
'''x = ("apple", "banana", "cherry")
y=list(x)
y[1]=("Kiwi")
x=tuple(y)
print(x)

#Add items
#Since tuples are immutable, they do not have a built-in append() method,
# for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

x=("apple", "banana", "cherry")
y=list(x)
y.append("kiwi")
x=tuple(y)
print(x)

#Add tuple to a tuple:so if we want to add one item, (or many), create a new tuple with the item(s), 
# and add it to the existing
thistuple = ("apple", "banana", "cherry")
y=("orange",)
thistuple+=y
print(thistuple)

#You cannot remove items in a tuple directly.
#instead Convert the tuple into a list, remove  and convert it back into a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple=tuple(y)
print(thistuple)'''

#The del keyword can delete the tuple completely:
thistuple=("apple","banana","cherry")
del thistuple
print(thistuple) 




