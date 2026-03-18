#1
#Write a function that takes any number of arguments and returns their sum.
def sum_all(*args):
    total=0
    for num in args:
        total+=num
    return total
print(sum_all(1,2,3))#6
print(sum_all(5,10))#15

#2
#Write a function that counts how many numbers are even in *args
def count_even(*args):
    even_count=0
    for num in args:
        if num%2==0:
            even_count+=1
    return even_count
print(count_even(1,2,3,4,6))#3




