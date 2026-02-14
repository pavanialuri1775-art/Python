#Adding Items:Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict={"name":"pavani",
          "course":"btech"
          }
thisdict["age"]=20
print(thisdict)#{'name': 'pavani', 'course': 'btech', 'age': 20}

#update dictionary:The update() method will update the dictionary with the items from a given argument. 
# If the item does not exist, the item will be added.
thisdict={"name":"pavani",
          "course":"btech"}
thisdict.update({"gender":"female","age":20})
print(thisdict)




