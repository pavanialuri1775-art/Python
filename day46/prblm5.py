#find the sum of even numbers in a list
lst=[1,2,3,4,5,6,7,8]
sum=0
for num in lst:
    if num%2==0:
        sum=sum+num
print(sum)