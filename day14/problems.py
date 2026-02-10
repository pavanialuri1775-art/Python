#problem1
#sort the list in ascending order
nums = [5,2,9,1,7]
nums.sort()
print(nums) #[1,2,5,7,9]

#Sort the list in descending order
nums=[5,2,9,1,7]
nums.sort(reverse=True)
print(nums) #[9, 7, 5, 2, 1]

#Sort the list of names alphabetically
names = ["Pavani","Ravi","Asha","Kiran"]
names.sort()
print(names)#['Asha', 'Kiran', 'Pavani', 'Ravi']

#Sort the list of fruits in reverse alphabetical order
fruits = ["apple", "banana", "mango", "grapes"]
fruits.sort(reverse=True)
print(fruits) #['mango', 'grapes', 'banana', 'apple']

#Use sorted() to sort the list without changing the original list
nums=[9,4,6,2]
newlist=sorted(nums)
print(nums)
print(newlist)

#Sort the names list in reverse order
names = ["Zara","Anu","Pavani","Bhavya"]
names.reverse()
print(names)

#First sort the list, then reverse it
nums = [4, 1, 3, 2]
nums.sort()
print(nums)
nums.reverse()
print(nums)

#Sort this list and print the smallest and largest element
nums = [45, 22, 89, 11, 67]
nums.sort()
print(nums)
print(nums[0])
print(nums[-1])

#Sort a list and print the second smallest number
nums = [9, 5, 2, 8, 1]
nums.sort()
print(nums[1])

#Sort the list of strings by length
words = ["apple","kiwi","banana","mango"]
words.sort(key=len)
print(words)

#Sort the list and check if it is already sorted
nums=[1,2,3,4]
if nums==sorted(nums):
    print("True")
else:
    print(False)







