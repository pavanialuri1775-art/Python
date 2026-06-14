#Reverse a list without using reverse()
arr=list(map(int,input("enter a number:").split(",")))
ans=[]
n=len(arr)
for i in range(n,0,-1):
    ans.append(arr[i])
print(ans)

#find the second largest number
arr=list(map(int,input("enter a number:").split(",")))
fst_largest=arr[0]
scnd_largest=arr[0]
for num in arr:
    if num<fst_largest and num>scnd_largest:
        scnd_largest=num
print("second_largest:",scnd_largest)

#7 Remove duplicates from a list
arr=list(map(int,input("enter a number").split(",")))
new_list=[]
for num in arr:
    if num not in new_list:
        new_list.append(num)
print(new_list)

#Move all zeros to the end
arr=list(map(int,input("enter a number:").split(",")))
non_zero=[]
zeroes=[]
for num in arr:
    if num==0:
        zeroes.append(num)
    else:
        non_zero.append(num)
s=non_zero+zeroes
print(s)
