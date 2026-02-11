#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1={"apple", "banana", "cherry"}
set2={"google", "microsoft", "apple"}
set3=set1.symmetric_difference(set2)
print(set3)

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
#Example
set1={"apple", "banana", "cherry"}
set2={"google", "microsoft", "apple"}
print(set1^set2)

#The symmetric_difference_update() method will also keep theitems that are not present in both sets
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)


