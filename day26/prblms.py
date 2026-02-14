#Create a dictionary and print the value of key "name".
'''thisdict={"name":"pavani",
          "age":20
          }
print(thisdict["name"])#pavani

#Change the value of key "b" to 50 and print the dictionary
d = {"a": 10, "b": 20, "c": 30}
d["b"]=50
print(d)#{'a': 10, 'b': 50, 'c': 30}

#Add a new key "d" with value 40 to the dictionary
d = {"a": 10, "b": 20, "c": 30}
d["d"]=40
print(d)#{'a': 10, 'b': 20, 'c': 30, 'd': 40}

#Remove the key "b" using pop().
d = {"a": 10, "b": 20, "c": 30}
d.pop("b")
print(d)#{'a': 10, 'c': 30}

#Print the sum of all values in the dictionary
d = {"a": 10, "b": 20, "c": 30}
k=d.values()
print(sum(k))

#Print only the values greater than 12.
d = {"a": 10, "b": 15, "c": 20}
s=d.values()
for x in s:
    if x>12:
        print(x)
        
#Count how many times 10 appears in the values
d = {"a": 10, "b": 20, "c": 10, "d": 30}
s=d.values()
k=list(s)
print(k.count(10))'''

#Create a new dictionary with keys and values swapped.
d = {"a": 10, "b": 20, "c": 30}
new_d={}
for x,y in d.items():
    new_d[y]=x
print(new_d)






