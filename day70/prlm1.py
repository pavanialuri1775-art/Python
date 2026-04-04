#Python JSON
#JSON is a syntax for storing and exchanging data.
#JSON is text, written with JavaScript object notation.
#JSON in Python
#Python has a built-in package called json, which can be used to work with JSON data.
#Parse JSON - Convert from JSON to Python
#If you have a JSON string, you can parse it by using the json.loads() method.
#ex:
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)#parse
print(y["age"])

#Convert from Python to JSON.
#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y)

