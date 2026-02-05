#Loop through a tuple
#we can loop through the tuple items by using a for loop.
#Iterate through the items and print the values
'''thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Loop Through the Index Numbers
#You can also loop through the tuple items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
#Print all items by referring to their index number
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])'''

#while loop
#we use len fun to determine length
#remember to increase 1 for each iteration
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1





