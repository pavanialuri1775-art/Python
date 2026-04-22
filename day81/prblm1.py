#iterators
#an iterator is an object that lets us to go through values one by one.
#it remembers the current position.
nums = [10, 20, 30]
it=iter(nums)
print(next(it))#10
print(next(it))#20
print(next(it))#30

#Iterable vs Iterator
#Iterable:ojects we can loop through
#list
#tuple
#string
#set 
#dictionary
#example
a = [1,2,3]
for i in a:
    print(i)

#Iterator:Object created from iterable using iter()
a = [1,2,3]
it = iter(a)
print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3
#print(next(it))   # stop iteration

#Strings are Iterable
s = "python"
it = iter(s)
print(next(it))   # p
print(next(it))   # y
print(next(it))   # t