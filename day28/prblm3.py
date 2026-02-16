#merge two dictionaries if keys overlap sum the values
d1 = {'a': 10, 'b': 20}
d2 = {"b":30,"c":40}
merge=d1.copy()
for k,v in d2.items():
    if k in merge:
        merge[k]+=v
    else:
        merge[k]=v
print(merge)