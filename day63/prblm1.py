#print numbers from 1 to n using recursion
def numbers(n):
    if n==0:#base condition
        return
    numbers(n-1)
    print(n)
numbers(5)#1 2 3 4 5

#print numbers from n to 1
def numbers(n):
    if n==0:
        return
    print(n)
    numbers(n-1)
numbers(5)#5 4 3 2 1 

#sum of first n numbers
def sum_numbers(n):
    if n==0:
        return 0
    return n+sum_numbers(n-1)
print(sum_numbers(5))#15
    