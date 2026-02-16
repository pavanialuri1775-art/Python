#Print only the keys.
d = {"a": 10, "b": 20, "c": 30}
for x in d:
    print(x)#a
            #b
            #c
            
#Print only the values.
d = {"a": 10, "b": 20, "c": 30}
for x in d:
    print(d[x])#10
                #20
                #30
                
#Change the value of key "b" to 50 and print the dictionary.
d = {"a": 10, "b": 20, "c": 30}
d["b"]=50
print(d)#{'a': 10, 'b': 50, 'c': 30}

#Add a new key "d" with value 40 and print the dictionary
d = {"a": 10, "b": 20, "c": 30}
d["d"]=40
print(d)#{'a': 10, 'b': 20, 'c': 30, 'd': 40}

#print the sum of the all values in the dictionary
d = {"a": 10, "b": 20, "c": 30}
k=d.values()
print(sum(k))#60

#create a new dictionary where values become their squares
d={"a":2,"b":3,"c":4}
for i in d:
    d[i]**=2
print(d)#{'a': 4, 'b': 9, 'c': 16}

#print the key whose value is maximum
d = {"a": 10, "b": 30, "c": 20}
k=list(d)
print(max(d,key=d.get))




    



