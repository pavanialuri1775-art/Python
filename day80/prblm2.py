#range() 
#range() is a built-in Python function used to generate a sequence of numbers.
#Mostly used in loops.
#range(start, stop, step)
#start → where numbers begin
#stop → where numbers end (excluded)
#step → gap between numbers
#range() with One Argument
for i in range(10):
    print(i)
#range() with Two Arguments
for i in range(3,10):
    print(i)
#range() with Three Arguments
for i in range(3,10,2):
    print(i)
    
#Convert range to list
print(list(range(5)))

#Slicing range
r = range(10)
print(r[2])
print(r[:3])
print(list(r[:3]))