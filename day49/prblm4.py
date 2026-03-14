#11
#average of numbers in a list
nums=[2,3,4,5]
i=0
total=0
n=len(nums)
while i<n:
    total+=nums[i]
    i+=1
average=total/n
print(average)

#12
#how many times a number appears in a list
nums=[2,4,2,5,2,7]
i=0
target=2
count=0
while i<len(nums):
    if nums[i]==target:
        count+=1
    i+=1
print(count)

        