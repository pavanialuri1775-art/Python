#Create a list and print all elements
arr = list(map(int,input("enter element:").split()))
for i in arr:
    print(i)
    
#2 Find the sum of all elements in a list
arr=list(map(int,input("enter a number:").split()))
sum=0
for i in arr:
    sum+=i
print(sum)

#3 Find the largest and smallest element
arr=list(map(int,input("enter a number:").split()))
largest_num=arr[0]
smallest_num=arr[0]
for num in arr:
    if num>largest_num:
        largest_num=num
    elif num<smallest_num:
        smallest_num=num
print(largest_num)  
print(smallest_num)

#Count how many times a number appears
arr=list(map(int,input("enter a number").split()))
freq={}
for num in arr:
        freq[num]=freq.get(num,0)+1
print(freq)
