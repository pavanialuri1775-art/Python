#Parse JSON
import json
data = '{"name": "Pavani", "age": 22, "city": "Hyderabad"}'
y=json.loads(data)
print(y["name"])
print(y["city"])

#convert DICT->JSON
import json
d={"course":"python","duration":"3 months"}
s=json.dumps(d)
print(s)

