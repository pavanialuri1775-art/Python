#lambda to add two numbers
x=lambda a,b:a+b
print(x(2,3))#5

#2
#lambda to check even or odd
x=lambda x:"odd" if x%2!=0 else "even"
print(x(5))#odd

#3
#use lambda with map()
lst=[2,3,4,5,6]
square=list(map(lambda x:x*x,lst))
print(square)#[4,9,16,25,36]

#4
#use lambda with filter
nums=list(range(1,21))
new_lst=list(filter(lambda x:x%2==0,nums))
print(new_lst)

#5
#sort list of tuples using lambda
my_lst=[(2,5),(1,3),(4,2)]
new_lst=sorted(my_lst,key=lambda x:x[1])
print(new_lst)