#dictonaries
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionaries are used to store data values in key:value pairs.
#Dictionaries are written with curly brackets, and have keys and values.

#Create and print a dictionary
thisdict={"name":"pavani", "age" : "20","branch": "Aiml"}
print(thisdict)#{'name': 'pavani', 'age': '20', 'branch': 'Aiml'}

#Dictionary Items
#Dictionary items are ordered, changeable, and do not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#Example
thisdict={
    "name":"pavani",
    "age":20
}
print(thisdict["name"])#pavani

#Dictionaries cannot have two items with the same key
#we use len() function to determine how many items a dictonary has
thisdict={
    "name":"pavani",
    "age":"20"
}
print(len(thisdict))#2

#The values in dictionary items can be of any data type
#String, int, boolean, and list data types
thisdict={"name" :"pavani",
          "year" :2005,
          "age":20
          }
print(thisdict)#{'name': 'pavani', 'year': 2005, 'age': 20}

#type()
#dictionaries are defined as objects with the data type 'dict'
thisdict={"name":"pavani","course":"btech"}
print(type(thisdict))#<class 'dict'>

#dict():we can use the dict() constructor to make a dictionary
thisdict=dict(name="pavani",age=20,country="India")
print(thisdict)#{'name': 'pavani', 'age': 20, 'country': 'India'}





