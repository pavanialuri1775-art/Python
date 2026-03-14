#16(set)
#how many elements are greater than 10
nums={23,11,5,6,7,8,99}
count=0
for num in nums:
    if num>10:
        count+=1
print(count)

#17 
#find the key with the largestvalue
scores = {
    "Alice": 88,
    "Bob": 95,
    "Charlie": 92,
    "David": 95
}
largest_value=0
for key in scores:
    if scores[key]>largest_value:
        largest_value=scores[key]
for key in scores:
    if scores[key]==largest_value:
        print(key)
    
#key with the smallest value
temperatures = {
    "Mumbai": 32,
    "Delhi": 28,
    "Kolkata": 28,
    "Chennai": 35
}
min_value=list(temperatures.values())[0]
for key in temperatures:
    if temperatures[key]<min_value:
        min_value=temperatures[key]
for key in temperatures:
    if temperatures[key]==min_value:
        print(key)
    