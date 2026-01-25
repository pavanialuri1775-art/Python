#Access characters
s = "python"
print(s[0]) #first character
print(s[-1])#last character

#String length
s = "education"
print(len(s))

#Indexing
s = "hello"
print(s[1]) #e
print(s[-1]) #o

#Iterate through string
s = "abc"
i=0
for ch in s:
    print(i,ch)
    i=i+1
    
# Concatenation
a = "Hello"
b = "World"
print(a+" "+b)#Combine with space
name=f"{a} {b}"
print(name)

#Slicing
s = "programming"
print(s[0:5]) #progr
print(s[7:]) #ming
print(s[3:8]) #gramm

#Step slicing
s = "abcdefgh"
print(s[0:7:2]) #alternate characters
print(s[0:7:3]) #Print every 3rd character

#Reverse except first character
s = "python"
print(s[0]+s[1:][::-1])

#Print from second last character to start
s = "hello"
print(s[-2::-1])

#Change case
s = "PyThOn"
print(s.upper())
print(s.lower())
print(s.swapcase()) 
