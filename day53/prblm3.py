#6
def sum_of_num(*args,**kwargs):
    total=0
    for i in args:
        total+=i
    for value in kwargs.values():
        total+=value
    return total
print(sum_of_num(1,2,3,a=4,b=5))

#7
def info(name,*marks):
    return sum(marks)/len(marks)
print(info("Pavani", 80, 90, 100))

#8
def multiply(a,b,c):
    return a*b*c
nums=[2,4,6]
print(multiply(*nums))#48

#9
def my_function(name,age):
    print(name,age)
data = {"name": "Pavani", "age": 20}
my_function(**data)

    