#remove():removes specified item from list.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop():The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#del:The del keyword also removes the specified index.
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the List:Clear() method empties the list.
#The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)



