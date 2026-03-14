#9
#count even and odd numbers in a list
nums=[1,2,3,4,5,6,7,8]
i=0
even_count=0
odd_count=0
while i<len(nums):
    if nums[i]%2==0:
        even_count+=1
    else:
        odd_count+=1
    i+=1
print("even_count:",even_count)
print("odd_count:",odd_count)

#10
#sum of all numbers in a list
nums=[2,4,5,6]
i=0
sum=0
while i<len(nums):
    sum+=nums[i]
    i+=1
print(sum)