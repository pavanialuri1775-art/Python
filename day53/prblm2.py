#3
#Write a function that prints all key-value pairs from **kwargs.
def my_function(**info):
    print("name:",info["name"])
    print("age:",info["age"])
my_function(name="Pavani",age=20)

#4
#Write a function that returns the sum of all values in **kwargs.
def sum_of_values(**kwargs):
    total=0
    for value in kwargs.values():
        total+=value
    return total
print(sum_of_values(a=10,b=20,c=5))#35

#5
#Write a function that checks if "age" exists in **kwargs.
def my_function(**kwargs):
    for key in kwargs:
        if "age" in kwargs:
            return True
    return False
print(my_function(name="Pavani",age=20))
print(my_function(name="Pavani"))


    


    
    
    