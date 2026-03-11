#check palindrome string
s=input("enter a string:")
rev=""
for ch in s:
    rev=ch+rev
if rev==s:
    print("palindrome")
else:
    print("not a palindrome")

#find smallest number in a list
lst=[15,45,23,89,12]
smallest_number=lst[0]
for num in lst:
    if num<smallest_number:
        smallest_number=num
print(smallest_number)
    
#find common elements in two lists
a=[1,2,3,4]
b=[3,4,5,6]
common=[]
for i in a:
    if i in b:
        common.append(i)
print(common)