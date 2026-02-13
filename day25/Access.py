#Accessing items:we can access the items of a dictionary by referring to its key name
thisdict={
    "brand":"puma",
    "year":1564
}
x=thisdict["brand"]
print(x)#puma

#we can also use the get() method
thisdict={
    "brand":"puma",
    "year":1564
}
x=thisdict.get("year")
print(x)#1564

#The keys() method will return a list of all the keys in the dictionary
thisdict={"brand":"puma",
    "year":1564
}
x=thisdict.keys()
print(x)#dict_keys(['brand', 'year'])        

#The values() method will return a list of all the values in the dictionary.
thisdict={"brand":"puma",
    "year":1564
}
x=thisdict.values()
print(x)#dict_values(['puma', 1564])

#The items() method will return each item in a dictionary, as tuples in a list.
thisdict={"brand":"puma",
    "year":1564
}
x=thisdict.items()
print(x)#dict_items([('brand', 'puma'), ('year', 1564)])

#in keyword:To determine if a specified key is present in a dictionary use the in keyword
thisdict={"brand":"puma",
    "year":1564
}
if "brand" in thisdict:
    print("yes")#yes


