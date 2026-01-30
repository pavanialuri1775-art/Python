#Create a list of 5 subjects and print the first and last subject.
thislist=["maths","english","science","social","hindi"]
print(thislist[0])
print(thislist[-1])

#Print the second last element of this list:
colors = ["red", "blue", "green", "yellow"]
print(colors[-2])

#Access and print each element using indexing (not loop).
colors = ["red", "blue", "green", "yellow"]
print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])

#Change the first element of the list to "Python"
langs = ["Java", "C", "C++"]
langs[0]="Python"
print(langs)

#Add "orange" at the end of the list
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)

#Insert "car" at index 1
vehicles = ["bike", "bus", "train"]
vehicles.insert(1,"car")
print(vehicles)

#Extend the list with another list
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)

#Remove "pen" from the list
items = ["book", "pen", "pencil"]
items.remove("pen")
print(items)

#Remove the last element using pop().
items = ["book", "pen", "pencil"]
items.pop()
print(items)
