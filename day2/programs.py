#multiple variable
a=b=c=10
print(a)
print(b)
print(c)

#data type
age=20
marks=15.5
name="pavani"
print(type(age))
print(type(marks))
print(type(name))

#age after 5years
age=20
print(int(age)+5)

#multiple assignment
age,name,marks=17,"Pavani",15.5
print("age:",age)
print("name:",name)
print("marks:",marks)

#swapping (using temp variable)
a=10
b=5
temp=a
a=b
b=temp
print("after swapping")
print("a=",a)
print("b=",b)
#without using temporary variable
a=10
b=5
a,b=b,a
print("after swapping")
print("a=",a)
print("b=",b)