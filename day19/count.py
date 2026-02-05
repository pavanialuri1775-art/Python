#Python has two built-in methods that you can use on tuples.
#count():Returns the number of times a specified value occurs in a tuple
#index():Searches the tuple for a specified value and returns the position of where it was found

nums = (1, 2, 3, 2, 4, 2)
#count how many times 2 appears
y=nums.count(2)
print(y) #3

#find the index of first 2
nums.index(2) #3

#Unpack this tuple
data = (100, 200, 300, 400, 500)
(a,*rest,b)=data
print(a) #first value →100
print(*rest)#middle values->rest
print(b)#last value-500

