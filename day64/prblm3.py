#13 Function with default argument
def greet(name="Guest"):
    return f"hello {name}"
print(greet())

#14 use *args
#Find sum of any number of inputs
def sum_of_nums(*args):
    result=0
    for i in args:
        result+=i
    return result
print(sum_of_nums(2,3,4,5,6))

#15 **kwargs
def key_value(**kwargs):
    return kwargs
data=key_value(name="pavani",age=20)
print(data)

#16 use **kwargs
#find sum of any numbers
def sum_of_nums(**kwargs):
    result=0
    for value in kwargs.values():
        result+=value
    return result
print(sum_of_nums(a=10,b=12,c=2))

#17 maximum value using kwargs
def maximum_value(**kwargs):
    return  max(kwargs.values())
print(maximum_value(a=10,b=50,c=30))


    
    