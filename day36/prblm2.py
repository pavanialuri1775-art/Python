#count even and odd numbers in a list
thelist=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
for i in thelist:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even",even)
print("odd",odd)

#remove duplicates
thelist=[1,2,1,2,3,4,5,6,7,2]
unique=[]
for i in thelist:
    if i not in unique:
        unique.append(i)
print(unique)
