#positional arguments:values are assigned based on the position.
def student(name,age):
    print("name:",name)
    print("Age:",age)
student("Pavani",20)

#Keyword Arguments:Arguments are passed using parameter names.
def student(name,age):
    print("name:",name)
    print("Age:",age)
student(age=20,name="pavani")

#Default arguments:Parameter gets a default value if no value is passed
def greet(name="Guest"):
    print("Hello", name)
greet()

#Variable-Length Arguments:Used when number of arguments is unknown.
#(a) *args
#stores multiple positional arguments in a tuple.
def add(*numbers):
    print(sum(numbers))
add(1,2,3,4)

#) **kwargs
#Stores multiple keyword arguments in a dictionary.
def details(**data):
    print(data)
details(name="Pavani", age=20)