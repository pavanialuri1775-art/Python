#4
#First duplicate number
'''nums=[3,5,2,7,5,9,2]
i=0
found=False
while i<len(nums):
    j=i+1
    while j<len(nums) and not found:
        if nums[i]==nums[j]:
            print(nums[i])
            found=True
            break
        j+=1
    i+=1
    
#5
#largest number in a list using while loop
nums=[7,3,10,4,5]
i=0
largest_num=nums[0]
while i<len(nums):
    if nums[i]>largest_num:
        largest_num=nums[i]
    i+=1
print(largest_num)#10

#6
#find the smallest number in a list
nums=[7,3,10,4,5]
i=0
smallest_num=nums[0]
while i<len(nums):
    if nums[i]<smallest_num:
        smallest_num=nums[i]
    i+=1
print(smallest_num)#3'''

#8
#find the second largest number using in a list
nums=[7,3,10,4,5]
i=0
first_largest=nums[0]
second_largest=nums[i]
while i<len(nums):
    if nums[i]>first_largest:
        second_largest=first_largest
        first_largest=nums[i]
    elif nums[i]>second_largest and nums[i]!=first_largest:
        second_largest=nums[i]
    i+=1
print(first_largest)
print(second_largest)
