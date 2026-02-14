#Loop Through a Dictionary
#we can loop through a dictionary using for loop
#while looping through the dictonaries return values are the keys but there are methods to return key values as well
'''thisdict={"name":"pavani",
          "branch":"AIML",
          "course":"btech"
          }
for x in thisdict:
    print(x)#name
            #branch
            #course'''
            
#Print all values in the dictionary, one by one
thisdict={"name":"pavani",
          "branch":"AIML",
          "course":"btech"
          }
for x in thisdict:
    print(thisdict[x])
    
#we can use the keys() method to return the keys of a dictionary
thisdict={"name":"pavani",
          "branch":"AIML",
          "course":"btech"
          }
for x in thisdict.keys():
      print(x)
      
#we can loop through both keys and values by using the items() method
thisdict={"name":"pavani",
          "branch":"AIML",
          "course":"btech"
          }
for x,y in thisdict.items():
    print(x,y)

    
