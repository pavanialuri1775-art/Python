#13 tuples with loops
#sum of elements
nums=(2,4,6,8)
i=0
total=0
while i<len(nums):
    total+=nums[i]
    i+=1
print(total)

#14
#sets with for loop
nums={2,4,6,8}
for i in nums:
    print(i)
    
#15
#dictonaries with for loop
student={"name":"pavani","course":"btech"}
for key in student:
    print(key,student[key])
    
#print keys
for key in student:
    print(key)
    
#print values
for value in student.values():
    print(value)
    
#print key value pairs
for key,value in student.items():
    print(key,value)
    