#Python for loop to iterate through a dictionary
the_dict={"name":"pavani",
          "age":20}
for i in the_dict:
    print(i,the_dict[i])
    
#
the_dict={"name":"pavani",
          "age":20}
for i,j in the_dict.items():
    print(i,j)
    
#Nested for loops in Python (one loop inside another loop)
list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']
for x in list1:
    for y in list2:
        print(x,y)