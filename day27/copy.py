#we can make a copy of a dictionary using the copy() method
thisdict= { "name":"pavani",
    "branch":"Aiml",
    "course":"btech" 
}
mydict=thisdict.copy()
print(mydict)

#we can also make a copy of dictionary using the dict() method
thisdict={"name":"pavani",
    "branch":"Aiml",
    "course":"btech"}
mydict=dict(thisdict)
print(mydict)
