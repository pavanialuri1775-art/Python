'''num=int(input("enter a number:"))
if (num&1==0):
    print("even")
else:
    print("odd")
    
#Create a list of 5 numbers, add a new number to it, and print the list.
numbers=[1,2,3,4,5]
numbers.append(6)
print(numbers)

#Create a list of numbers [1, 2, 3, 4, 5]. Convert it into a tuple and print it.
list=[1,2,3,4,5]
y=tuple(list)
print(y)

#Create a tuple with values (10, 20, 30) and unpack the values into three variables, then print them.
thistuple=(10,20,30)
a,b,c=thistuple
print(a)
print(b)
print(c)'''

#
item1=120.50
item2=80.75
item3=50.25
total_price=item1+item2+item3
final_bill=total_price*0.18+total_price
print(final_bill)

#extract interview from given string
name="PythonInterview"
print(name[6:])
print(name.lower())

#
age=16
has_id=True
if age>=18 or has_id==True:
    print("Allowed")
else:
    print("Not Allowed")
    
#
math=78.25
science=82.25
english=69.75
sum=math+science+english
average_marks=sum/3
print(round(average_marks,2))

#
name="PythonIsFun"
print(name[0:6])
print(name[1:-1:2])