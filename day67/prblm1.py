#1 create a generator that yields numbers from 1 to n
def my_generator(n):
    for i in range(1,n+1):
        yield i
for num in my_generator(5):
    print(num,end=" ")
    
#2 Even Numbers Generator
def even_num(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
for num in even_num(10):
    print(num,end=" ")
    
#3 fibonacci generator
def fibonacci_num(n):
    a,b=0,1
    for i in range(0,n):
        yield a
        a,b=b,a+b
for num in fibonacci_num(5):
    print(num,end=" ")
        
        
    
    