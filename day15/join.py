# to join two or more lists we use "+" operator
'''list1 = ["a","b","c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#Append list2 into list1
list1 = ["a","b","c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)'''

#extend() method is to add elements from one list to another list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)



