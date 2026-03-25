#Lambda with Built-in Functions.
#Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().
#using lambda with map()
#The map() function applies a function to every item in an iterable
#ex:triple all numbers in a list.
numbers=[1,2,3,4,5]
tripled=list(map(lambda x:x*3,numbers))
print(tripled)#[3, 6, 9, 12, 15]

#using lambda with filter()
#The filter() function creates a list of items for which a function returns True
#Filter out odd numbers from a list
numbers=[1,2,3,4,5,6,7,8]
odd_numbers=list(filter(lambda x:x%2!=0,numbers))
print(odd_numbers)#[1, 3, 5, 7]

#Using Lambda with sorted()
#The sorted() function can use a lambda as a key.
#Sort strings by length.
words = ["apple", "pie", "banana", "cherry"]
sorted_words=sorted(words,key=lambda x:len(x))
print(sorted_words)#['pie', 'apple', 'banana', 'cherry']




