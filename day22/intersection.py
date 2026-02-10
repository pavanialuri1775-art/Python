#Intersection:Keep ONLY the duplicates
#Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3) #{'apple'}

#Use & to join two sets
set1={"apple", "banana", "cherry"}
set2={"google", "microsoft", "apple"}
set3=set1 & set2
print(set3) #{'apple'}

#The intersection_update() method will also keep ONLY the duplicates,
# but it will change the original set instead of returning a new set.
#Keep the items that exist in both set1, and set2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1) #{'apple'}

#The values True and 1 are considered the same value. The same goes for False and 0.
set1={"apple", 1,  "banana", 0, "cherry"}
set2={False, "google", 1, "apple", 2, True}
set3=set1.intersection(set2)
print(set3) #{False, 1, 'apple'}














