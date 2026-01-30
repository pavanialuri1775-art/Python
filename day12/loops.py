#Loop Through a List:we can loop through the list using a for loop.
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
#Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Using a While Loop:
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
  #List Comprehension offers the shortest syntax for looping through lists
#List comprehension is a shortcut for writing a for loop inside a list.

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]





