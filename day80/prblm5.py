#Loop Problem
'''n=int(input("enter any number:"))
for i in range(n):
    print(i*i)'''

#Find Missing Number
a = [1,2,3,5]
total=0
for i in range(6):
    total+=i
print(total-sum(a))