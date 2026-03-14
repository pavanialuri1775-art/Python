#20
students = {
    "Alice": 88,
    "Bob": 75,
    "Charlie": 92,
    "David": 67
}
count=0
for key in students:
    if students[key]%2==0:
        count+=1
        print(key)
print("number of students with even score:",count)
    