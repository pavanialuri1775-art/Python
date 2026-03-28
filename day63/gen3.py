#Generator Expressions:Similar to list comprehensions,
# you can create generators using generator expressions with parentheses instead of square brackets
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

## Calculate sum of squares without creating a list
total= sum(x * x for x in range(5))
print(total)#30

#Fibonacci Sequence Generator
#Generators can be used to create the Fibonacci sequence.
#Generate 10 Fibonacci numbers
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
gen=fibonacci()
for i in range(10):
    print(next(gen))
    
