def containsDuplicate(nums) -> bool:
    if len(nums)!=len(set(nums)):
        return True
    else:
        return False