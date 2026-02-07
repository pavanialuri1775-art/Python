#Once a set is created, we cannot change its items, but we can add new items.
#To add one item to a set use the add() method.
#example
#Add an item to a set, using the add() method:
'''thisset={"apple","banana","cherry"}
thisset.add("orange")
print(thisset)'''

#Add Sets
#To add items from another set into the current set, use the update() method.
thisset={"apple","banana","cherry"}
tropical = {"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)

#the object in the update()method does not have to be a set,
# it can beany iterable objects (tuples,lists,dictonaries)
#Add elements of a list to a set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)









