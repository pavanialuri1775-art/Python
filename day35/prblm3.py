#counting vowels in a string
'''n=input("enter a string:")
count=0
vowels="AEIOUaeiou"
for ch in n:
    if ch in vowels:
        count+=1
print(count)

#find largest number in a list
thelist=[23,45,66,78,99,33]
largest=0
for i in thelist:
    if i>largest:
        largest=i
print(largest)#99'''

#second max number in a list
thelist=[23,45,66,78,99,33]
largest=thelist[0]
second_largest=thelist[0]
for i in thelist:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!=largest:
        second_largest=i
print("largest:",largest)
print("Second largest:",second_largest)

    