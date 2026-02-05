#Create a tuple of 5 subjects 
subjects=("maths","EVS","Science","telugu","hindi")
#print the first element
print(subjects[0])# maths
#print the last element using negative indexing
print(subjects[-1])#hindi

#Tuple Packing
#pack your name, age, branch into a tuple and print it.
thistuple=("pavani","20","CSM")
print(thistuple) #('pavani', '20', 'CSM')

#Unpack this tuple and print each value
t = ("Python", 3.10, "Beginner")
a,b,c=t
print(a)
print(b)
print(c)

#Slice a Tuple
nums=(10,20,30,40,50,60)
#print elements from index 1 to 4
print(nums[1:4])
#last three elements
print(nums[3:])

#Change Tuple
colors = ("red", "blue", "green")
#Change "blue" to "yellow"
y=list(colors)
y[1]="yellow"
colors=tuple(y)
print(colors)

#Write code to check whether "apple" exists in this tuple
fruits = ("banana", "mango", "apple", "grapes")
print("apple" in fruits)

#Create a tuple with one element and print its type.
name=("pavani",)
print(type(name))




