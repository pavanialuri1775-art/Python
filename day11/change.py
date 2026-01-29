#Change Item Value :To change the value of a specific item, refer to the index number
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#insert():to insert a item in the list at a specified index we se insert() method
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append()-To add an item to the end of the list,we use the append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extend():to append the elements from the another list to the current list.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



