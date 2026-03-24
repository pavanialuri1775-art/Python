#Nested condition
nums=[10,15,20,25,30]
lst=["both"if x%2==0 and x%5==0
     else "two" if x%2==0
     else "five"
     for x in nums]
print(lst)