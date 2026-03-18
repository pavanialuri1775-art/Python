#Arbitrary Keyword Arguments - **kwargs
'''If you do not know how many keyword arguments will be passed into your function,
add two asterisks ** before the parameter name.'''
#This way, the function will receive a dictionary of arguments and can access the items accordingly

#ex
def my_function(**kid):
    print("my last name is "+kid["lname"])
my_function(fname="Pavani",lname="Aluri")

#Arbitrary Keyword Arguments are often shortened to **kwargs in Python documentation
#**Kwargs:The **kwargs parameter allows a function to accept any number of keyword arguments.
#Inside the function, kwargs becomes a dictionary containing all the keyword arguments.
#ex
#Accesing values from **kwargs
def my_function(**myvar):
    print("Type:",type(myvar))#Type: <class 'dict'>
    print("Name:",myvar["name"])#Name: pavani
    print("Age:",myvar["age"])#Age: 20
    print("All data:",myvar)
my_function(name='pavani',age=20,city="IBP")

#Using **kwargs with Regular Arguments
#regular parameters must come before **Kwargs
#example
def my_function(student_name,**info):
    print("student_name:",student_name)#student_name: pavanialuri
    print("Additional details:")#Additional details:
    for key,value in info.items():
        print(" ",key+":",value)
my_function("pavanialuri",age="20",city="IBP",hobby="coding")# age: 20
                                                             # city: IBP
                                                             # hobby: coding


        
