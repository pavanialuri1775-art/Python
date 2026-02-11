#frozenset is an immutable version of a set.
#Like sets, it contains unique, unordered, unchangeable elements
#Unlike sets, elements cannot be added or removed from a frozenset.

#Creating a frozenset
#we use the frozenset() constructor to create a frozen set from any iterable.
#Create a frozenset and check its type:
x=frozenset({"Pavani","Geetha","Keerthi"})
print(x)
print(type(x))

#Being immutable means you cannot add or remove elements. 
# However, frozensets support all non-mutating operations of sets.
#copy()
x=frozenset({1,2,3})
k=x.copy()
print(x)
print(k)

#difference()
a=frozenset({1,2,3})
b=frozenset({3,4,5})
print(a.difference(b))

#intersection()	
a=frozenset({1,2,3})
b=frozenset({3,4,5})
print(a&b)

#union()
a=frozenset({1,2,3})
b=frozenset({3,4,5})
print(a|b)

#symmetric_difference()	
a=frozenset({1,2,3})
b=frozenset({3,4,5})
print(a^b)





