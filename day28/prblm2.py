d={
    "a":10,
    "b":15,
    "c":10,
    "d":20,
    "e":15
}
print(max(d,key=d.get))
new_dict={}
for x,y in d.items():
    if y not in new_dict:
        new_dict[y]=[x]
    else:
        new_dict[y].append(x)
print(new_dict)
count_dict={}
for v in d.values():
    if v not in count_dict:
        count_dict[v]=1
    else:
        count_dict[v]+=1
print(count_dict)
new_dict={}
for v in d:
    d[v]**=2
print(d)
d={
    "a":10,
    "b":15,
    "c":10,
    "d":20,
    "e":15
}
l_dict={}
for k,v in d.items():
    if v<=15:
        l_dict[k]=v
print(l_dict)

