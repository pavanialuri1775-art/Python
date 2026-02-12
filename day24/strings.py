#conversion of string to int
'''a=input("Enter a string:")
b=input("Enter a string:")
c=int(a)
d=int(b)
print(c+d)
print(c-d)
print(c*d)
print(c%d)

#string methods
s=input("Enter a string:")
print(s.upper())
print(s.lower())
print(s.title())

s=" Aluri Pavani"
print(s.strip())
print(s.replace("Aluri","Alluri"))

s="Pavani"
print(s.count("a"))

s="pavani"
count=0
consonants=0
vowels="aeiou"
for ch in s:
    if ch in vowels:
        count=count+1
    else:
        consonants=consonants+1
print(count)
print(consonants)

#counting consonants
s="pavani"
vowels="aeiou"
consonants=0
for ch in s:
    if ch not in vowels:
        consonants=consonants+1
print(consonants)

#index
s="Pavani"
print(s.index("P"))

#title:convert the first letter of each word to uppercase
#Capitalize:convert the first character of a string to uppercase
s="pavani"
print(s.capitalize())

#swapcase:converts uppercase to lowercase and lowercase to uppercase
s="PaVaNi"
print(s.swapcase())

#find:returns the index of first occurence of character
s="Pavani"
print(s.find("a"))

#startswith:check whether the string starts with given substring
s="Pavani"
print(s.startswith("Pa"))


#endswith:check whether the string ends with given substring
s="Pavani"
print(s.endswith("ni"))

#replace
s="Pavani"
print(s.replace("v","l")) #palani'''

#lstrip:removes the space from the left side of the string
s=" pavani"
print(s.lstrip())

#rstrip:removes space from the right side of the string
s="Pavani "
print(s.rstrip())

#split():splits the string
s="i am pavani"
print(s.split())

#join():used to join list items into a string using seperator
s=["i","am","pavani"]
print("".join(s))







    
    








