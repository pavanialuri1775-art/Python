#
def sum_of_even(n):
    total=0
    for i in range(2,n+1):
        if i%2==0:
            total+=i
    return total
print(sum_of_even(4))