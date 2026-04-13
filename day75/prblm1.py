#regex is a pattern matching tool used in:
#data extraction
#search text
#validate input
#replace pattern 

#ex:
#emails
#phonenumbers
#only digits

#ex1
import re
s = "a1b2c3"
x=re.findall("\d",s)
print(x)

#ex2 Extract all words
import re
s = "Hello 123 world!"
x=re.findall("[A-Za-z]+",s)
print(x)