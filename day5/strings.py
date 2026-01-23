#string:collection of characters enclosed with single quotes or double quotes

#assinging a string to a variable
name="pavani"
print(name) 

#Multiline strings
#we can assign a multiline string to a variable by using three quotes
#ex:
x='''i am A.pavani,i am currently pursuing my b.tech 3rd year in AIML from gurunanak 
institute of technology'''
print(x)

#strings are like arrays
#in python,a string behaves like an array of characters
#example for string "cat"
#Index	Character
#0	        c
#1	        a
#2	        t
#so,internally python treats it like ['c','a','t']

#Unicode characters
#Python strings store Unicode characters, which means:
#They can store English letters
#Numbers
#symbols 

#No separate character data type
#Python does not have a char data type.
#A single character is also a string, but its length is 1.
#example
ch = "A"
print(type(ch))  
print(len(ch))

#Access characters using square brackets [ ]
#You can access characters in a string using index numbers.
name="pavani"
print(name[0])
print(name[4])
print(name[-1]) #last character

#Looping Through a String
#Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
    print(x)
    
#String Length
#To get the length of a string, use the len() function.
Name="pavani"
print(len(Name))

#Check String
#To check if a certain phrase or character is present in a string, we can use the keyword in.
name="pavani"
print("n" in name)
print("S" in name)

#Check if NOT
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
name="sun rises in the east"
print("east"not in name)




