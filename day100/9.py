def missingNumber(nums):
    nums.sort()
    n=len(nums)
    total=0
    for i in range(1,n+1):
        total+=i
    return total-sum(nums)