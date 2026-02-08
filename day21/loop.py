#we can loop through the set items by using a for loop
#Loop through the set, and print the values
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
#Add elements
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
fruits={"mango","grapes"}
thisset.update(fruits)
print(thisset)

#Remove Elements
thisset={"red", "blue", "green"}
thisset.remove("blue")
thisset.discard("yellow")
print(thisset)

# Update a Set
set1={1, 2, 3}
set2={3, 4, 5}
set1.update(set2)
print(set1)

#Clear a Set
thisset={10,20,30,40}
thisset.clear()
print(thisset) #set()

#
attendees = {"Alice", "Bob", "Charlie"}
#A new student "David" joins → add him
attendees.add("david")
attendees.remove("Charlie")
print(attendees)






