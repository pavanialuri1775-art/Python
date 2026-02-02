#Add "grapes" to the end
'''fruits = ["apple","banana"]
fruits.append("grapes")
print(fruits) #['apple', 'banana', 'grapes']

#Insert "orange" at index 1
fruits = ["apple","mango"]
fruits.insert(1,"orange")
print(fruits) #['apple', 'orange', 'mango']

#Extend the list with another list
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)

#Add multiple items using extend()
nums = [10, 20]
add=[30,40,50]
nums.extend(add)
print(nums)

#Remove "maths" from the list
subjects = ["maths", "science", "english"]
subjects.remove("maths")
print(subjects)

#Remove the last element using pop()
colors = ["red","blue","green"]
colors.pop(-1)
print(colors)

#Delete the first element using del
nums = [10,20,30]
del nums[0]
print(nums)

#Clear the entire list
nums = [5, 6, 7]
nums.clear()
print(nums)

#Copy a list using copy() and modify the copy
a = [1, 2, 3]
b=a.copy()
b.append(4)
print(b)
print(a)

#Copy a list using list() and remove one item from the new list.
num=[1,2,3,4]
mylist=list(num)
mylist.remove(4)
print(mylist)'''

#Copy a list using slicing [:] and change one element.
num=[1,2,3,4]
new=num[:]
new[1]=7
print(new)






