#The difference() method will return a new set that will contain only
# the items from the first set that are not present in the other set.

#Keep all items from set1 that are not in set2
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set3=set1.difference(set2)
print(set3) #{'cherry', 'banana'}

#We can use the - operator instead of the difference() method, and you will get the same result.
#Use - to join two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3) #{'cherry', 'banana'}

#The difference_update() method will keep the items from the first set that are not in the other set,
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1) #{'banana', 'cherry'}  








