#7 Datatypes + Loops
#Find the largest number in a list
lst = [10, 45, 23, 89, 12]
largest=lst[0]
for num in lst:
    if num>largest:
        largest=num
print(largest)

#8 Count vowels in a string
n=input("enter a string:")
count=0
vowels="AEIOUaeiou"
for ch in n:
    if ch in vowels:
        count+=1
print(count)

#9 Dictionary
#Print keys and values using loop
d = {"a":1,"b":2,"c":3}
for i,j in d.items():
    print(i,j)
    
