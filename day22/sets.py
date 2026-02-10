#joining  sets using union() method
set1={1, 2, 3}
set2={3, 4, 5}
set3=set1.union(set2)
print(set3) #{1, 2, 3, 4, 5}

#join two sets using the | operator?
A={1, 2}
B={3, 4}
C={5, 6}
D=A|B|C
print(D) #{1, 2, 3, 4, 5, 6}

#Join a Set and a Tuple
#The union() method allows us to join a set with other data types, like lists or tuples.
x={"a","b","c"}
y = (1,2,3)
z = x.union(y)
print(z) #{1, 2, 3, 'b', 'a', 'c'}

#The update() method inserts the items in set2 into set1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)







