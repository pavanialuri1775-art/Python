#second largest number
lst=[10,45,23,89,12]
first_largest=lst[0]
second_largest=lst[1]
for num in lst:
    if num> first_largest: 
        second_largest=first_largest
        first_largest=num
    elif num>second_largest and num!=first_largest:
        second_largest=num
print(first_largest)
print(second_largest)

#reverse a string using loop
s=input("enter a string:")
rev=""
for ch in s:
    rev=ch+rev
print(rev)
        
