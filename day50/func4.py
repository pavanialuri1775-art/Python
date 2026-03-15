#keyword arguments
#we can send arguments withg the key=value syntax
def my_function(animal,name):
    print("I have a", animal)
    print("my",animal,"name is",name)
my_function(animal="dog",name="Buddy")

#positional arguments
#When we call a function with arguments without using keywords, they are called positional arguments.
#positional arguments must be in the correct order
def my_function(animal,name):
    print("I have a",animal)
    print("My",animal+"'s name is",name)
my_function("dog","puppy")

#Mixing Positional and Keyword Arguments
#we can mix positional and keyword arguments in a function call.
def my_function(animal,name,age):
    print("I have a",age,"years old",animal,"named",name)
my_function("dog",name="puppy",age=5)

#Passing Different Data Types
#we can send any data type as an argument to a function (string, number, list, dictionary, etc.).
def my_function(my_list):
    for fruit in my_list:
        print(fruit)
my_list=["pavani","geetha","keerthi"]
my_function(my_list)

#sending dictionay as an argument
def my_function(person):
    print("Name:",person["name"])
    print("Age:",person["age"])
my_person={"name":"pavani","age":20}
my_function(my_person)
    