#The findall() Function:The findall() function returns a list containing all matches.
#example
import re
txt="The rain in Spain"
x = re.findall("ai", txt)
print(x)

#example2
import re
txt="The rain in Spain"
x = re.findall("portugal", txt)
print(x)

#The search() Function
#The search() function searches the string for a match, and returns a Match object if there is a match.
#example
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())#3
#If no matches are found, the value None is returned
import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)#none


