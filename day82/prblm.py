#Datetime
#Python Dates
#A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
#ex:
import datetime
x = datetime.datetime.now()
print(x)
#The datetime module has many methods to return information about the date object.
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))#Friday

#Create a date object
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

#The strftime() Method
#The method is called strftime(), and takes one parameter, format, to specify the format of the returned string
#Display the name of the month
import datetime
x = datetime.datetime(2005,7,17)
print(x.strftime("%A"))

