#6
#sum of all values using args
def sum_of_values(*args):
    total=0
    for num in args:
        total+=num
    return total
print(sum_of_values(2,3,4,5,6))#20

#7
#find maximum using args
def maximum_value(*args):
    max_value=args[0]
    for num in args:
        if num>max_value:
            max_value=num
    return max_value
print(maximum_value(23,5,6,12,68,239))#239

#8
#print all key value pairs using kwrags
def key_value(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
key_value(name="pavani",age=20)


#9
#create function that prints student details using kwargs
def student_info(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
student_info(sname="Pavani",sage=20,course="btech")

#10
#combine args and kwargs in one function
def add(*args,**kwargs):
    print("args:",args)
    print("kwargs:")
    for key,value in kwargs.items():
        print(f"{key} : {value}")
add(4,5,a=2,b=8)

        