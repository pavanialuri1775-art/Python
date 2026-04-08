#Format the result
#son.dumps() method has parameters to make easier to read the result.
#we use indent parameters to define the number of  indents.
import json
x = {
  "name": "John",
  "age": 30}
print(json.dumps(x, indent=4))
#we use seperators parameter to change the default parameter.
print(json.dumps(x, indent=4, separators=(". ", " = ")))
#Use the sort_keys parameter to specify if the result should be sorted or not
print(json.dumps(x, indent=4, sort_keys=True))