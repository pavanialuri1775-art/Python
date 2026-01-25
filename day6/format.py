#String Format:As we learned in the Python Variables chapter, we cannot combine strings and numbers
#But we can combine strings and numbers by using f-strings or the format() method!
#F-strings
#example:
age = 36
txt = f"My name is John, I am {age}" #My name is John, I am 36
#f before the string → tells Python this is an f-string
#{age} → placeholder (Python replaces it with the value of age)

#Placeholders:
#variables
#expression
#calculations
#formating rules

price = 59
txt = f"The price is {price} dollars"
print(txt)  #The price is 59 dollars

#Modifiers (Formatting Values)
#Modifiers control how the value looks.
#.2fshow 2 decimal places
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) #The price is 59.00 dollars











