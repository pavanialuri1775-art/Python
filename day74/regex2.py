#The split() Function
#The split() function returns a list where the string has been split at each match.
#example:Split at each white-space character.
import re
txt = "The rain in Spain"
x = re.split("\s",txt)
print(x)#['The', 'rain', 'in', 'Spain']

#we can control the number of occurrences by specifying the maxsplit parameter.
#Split the string only at the first occurrence
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)#['The', 'rain in Spain']

#The sub() Function:
#The sub() function replaces the matches with the text of your choice.
#Replace every white-space character with the number 9.
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
#You can control the number of replacements by specifying the count parameter.
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)