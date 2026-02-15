#Nested Dictionaries:A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily={
    "child1":{
        "name":"chandu",
        "year":2001
        },
"child2":{
    "name":"prashu",
    "year":2003
},
"child3":{
    "name":"pavani",
    "year":2005
}
}
print(myfamily)#{'child1': {'name': 'shekar', 'year': 2001},
               #'child2': {'name': 'prashu', 'year': 2003}, 
               # 'child3': {'name': 'pavani', 'year': 2005}
               
#Access Items in Nested Dictionaries:To access items from a nested dictionary,
# you use the name of the dictionaries, starting with the outer dictionary
#Print the name of child 2
print(myfamily["child2"]["name"])#prashu

#Loop Through Nested Dictionaries

for x,obj in myfamily.items():
    print(x)
    for y in obj:
        print(y,":",obj[y])
'''child1
name : chandu
year : 2001
child2
name : prashu
year : 2003
child3
name : pavani
year : 2005'''









 