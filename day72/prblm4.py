#Working with Lists in JSON
#Access Nested Data
import json
data =''' {
    "students": [
        {"name": "A", "marks": 80},
        {"name": "B", "marks": 90},
        {"name": "C", "marks": 85}
    ]
}'''
parsed=json.loads(data)
for student in parsed["students"]:
    print(student["name"])

#Find Highest Marks
#Student with highest marks
import json
data =''' {
    "students": [
        {"name": "A", "marks": 80},
        {"name": "B", "marks": 90},
        {"name": "C", "marks": 85}
    ]
}'''
parsed=json.loads(data)
max_student = max(parsed["students"], key=lambda x: x["marks"])
print(max_student["marks"])
