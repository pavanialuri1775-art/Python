#add()
set1={1,2,3}
set2=set1.add(4)
print(set1)#{1, 2, 3, 4}

#clear()
set1={1,2,3,4}
print(set1.clear())#None

#copy()
set1={"apple","banana","cherry"}
set2=set1.copy()
print(set2)#{'cherry', 'banana', 'apple'}

#difference()
set1={1,2,3,4}
set2={2,3,4}
set3=set1.difference(set2)
print(set3)#{1}

#difference_update()
set1={1,2,3,4}
set2={2,3,4}
set1.difference_update(set2)
print(set1)#{1}

#discard()
set1={1,2,3,4}
set2=set1.discard(3)
print(set1)

#intersection()
set1={1,2,3,4,5}
set2={4,5,6,7}
set3=set1.intersection(set2)
print(set3)

#intersection_update()
set1={1,2,3,4,5}
set2={3,4,5}
set1.intersection_update(set2)
print(set1)

#pop()
set1={1,2,3,4}
set1.pop()
print(set1)

#remove()
set1={1,2,3,4}
set1.remove(3)
print(set1)

#union()
set1={1,2,3,4}
set2={3,4,5}
set3=set1.union(set2)
print(set3)

#update()
set1={1,2,3,4}
set2={3,4,5}
set1.update(set2)
print(set1)

#symmetric_difference()
set1={1,2,3,4}
set2={4,5,6}
set3=set1.symmetric_difference(set2)
print(set3)

#symmetric_difference_update()
set1={1,2,3,4}
set2={4,5}
set1.symmetric_difference_update(set2)
print(set1)