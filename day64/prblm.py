#1 write a function to return square of a number.
def square(n):
    return(n*n)
print(square(9))#81

#2 : Even/Odd
def even_or_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "odd"
n=int(input())
print(even_or_odd(6))

#3 Largest of 3 numbers
def largest_number(a,b,c):
    return max(a,b,c)
print(largest_number(23,12,36))

#4 sum of list
def sum_of_list(lst):
    total=0
    for i in lst:
        total+=i
    return total
my_list=[1,2,3,4]
print(sum_of_list(my_list))#10

#5 count vowels in a string
def vowel_count(s):
    count=0
    for ch in s:
        if ch in "AEIOUaeiou":
            count+=1
    return count
print(vowel_count("pavani"))