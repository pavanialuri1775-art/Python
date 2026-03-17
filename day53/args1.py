#Arbitary Arguments-*args
#when we do not know how many arguments will be passed into function,*args is added before the parameter name
#This way, the function will receive a tuple of arguments and can access the items accordingly.
#example
def my_function(*students):
    print("the person with rollno2 is "+students[1])
my_function("Pavani","Geetha","keerthi")#the person with rollno2 is Geetha

#*args
#The *args parameter allows a function to accept any number of positional arguments.
#Inside the function, args becomes a tuple containing all the passed arguments.
#ex
def my_function(*args):
    print("Type",type(args))#Type <class 'tuple'>
    print("first student:",args[0])#first student: pavss
    print("second student:",args[1])#second student: geethzz
    print("All students:",args)#All students: ('pavss', 'geethzz', 'avnsh')
my_function("pavss","geethzz","avnsh")

#Using *args with Regular Arguments
#You can combine regular parameters with *args.
#Regular parameters must come before *args.
def my_function(greeting,*names):
    for name in names:
        print(greeting,name)
my_function("Hello","pavss","sindu","lavss","teju","madhu")
#In this example, "Hello" is assigned to greeting, and the rest are collected in names.

#*args is useful when you want to create flexible functions.
#A function that calculates the sum of any number of values
def sum_of_numbers(*numbers):
    total=0
    for num in numbers:
        total+=num
    return total
print(sum_of_numbers(2,8,9,3))#22
print(sum_of_numbers(10,20,30))#60
print(sum_of_numbers(5))#5




