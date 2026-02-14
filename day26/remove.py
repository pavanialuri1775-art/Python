#Removing dictionary items:
#The pop() method removes the item with the specified key name
thisdict={"name":"pavani",
          "branch":"AIML",
          "course":"btech"
          }
thisdict.pop("branch")
print(thisdict)#{'name': 'pavani', 'course': 'btech'}

#popitem():popitem() method removes the last inserted item
thisdict={"name":"pavani",
          "branch":"AIML",
          "course":"btech"
          }
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name
#The del keyword can also delete the dictionary completely
thisdict={"name":"pavani",
          "branch":"AIML",
          "course":"btech"
          }
del thisdict["course"]
print(thisdict)#{'name': 'pavani', 'branch': 'AIML'}

#The clear() method empties the dictionary
thisdict={"name":"pavani",
          "branch":"AIML",
          "course":"btech"
          }
thisdict.clear()
print(thisdict)

