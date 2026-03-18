#Combining *args and **kwargs
#we can use both *args and **kwargs in the same function
#the order must be:
#regular parameters
#*args
#**kwargs
def my_function(title,*args,**kwargs):
    print("Title:", title)#Title: student Info
    print("Positional arguments:", args)#Positional arguments: ('pavani', 'aluri')
    print("Keyword arguments:", kwargs)#Keyword arguments: {'age': 20, 'city': 'Ibp'}      
my_function("student Info","pavani","aluri",age=20,city="Ibp")

#Unpacking Arguments
#The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
#ex:unpacking lists with *
#Using * to unpack a list into arguments
def my_function(a,b,c):
    return a+b+c
numbers=[1,2,3]
result=my_function(*numbers)
print(result)

#Unpacking Dictionaries with **
#ex:
def my_function(fname, lname):
      print("Hello", fname, lname)
person = {"fname": "Pavani", "lname": "Aluri"}
my_function(**person) 



    