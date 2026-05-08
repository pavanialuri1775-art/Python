class Solution:
    def intersection(self, nums):
        s=set(nums[0])
        for sublst in nums:
           s=s&set(sublst)
        return sorted(list(s))
    
class Solution:
    def findDifference(self, nums1,nums2):
        return [list(set(nums1)-set(nums2)),list(set(nums2)-set(nums1))]
    
    
class Solution:
    def maximumValue(self, strs):
        lst=[]
        for word in strs:
            if word.isdigit():
                lst.append(int(word))
            else:
                lst.append(len(word))
        return max(lst)
    
                