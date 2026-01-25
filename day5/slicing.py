#slicing:extracting a part of string using index positions.
#string[start : end : step]
#start:index to start
#end:index to stop
#step:how many steps to jump 

#example:
s="pavani"
print(s[0:3]) #pav
print(s[2:5]) #van

#Slice From the Start
#When we don’t give the start index, Python automatically starts from the first character (index 0).
s="pavani"
print(s[:5])

s="hello world"
print(s[:5])

#slice to the end
#When we don’t give the end index, Python will take characters till the end of the string.
s="pavani"
print(s[2:])

b = "Hello, World!"
print(b[7:])

#negative indexing:negative indexing means counting characters from the end of the string.
s="pavani"
print(s[-5:-1])

b = "Hello, World!"
print(b[-6:-1])

#reversing a string using step function
s="pavani"
print(s[::-1])







