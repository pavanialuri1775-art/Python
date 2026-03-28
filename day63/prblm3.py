#power function
def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)
print(power(2,3))#8

#fibonacci number
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))#5

#sum of array
def sum_array(numbers):
    if len(numbers)==0:
        return 0
    else:
        return numbers[0]+sum_array(numbers[1:])
my_list=[1,2,3,4]
print(sum_array(my_list))#10
    
    
