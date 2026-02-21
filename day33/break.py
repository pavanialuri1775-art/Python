#The break Statement:the break statement  is used to stop a loop even if the condition is still true.
#we use break when
#we find what we are looking for 
#we dont want to continue looping any more.
#example:
# Exit the loop when x is "banana"
'''names=["pavani","Geetha","Keerthi"]
for x in names:
    print(x)
    if x=="Geetha":
        break#pavani
              #Geetha
    
#Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)#apple'''

#search in a list
nums=[10,20,30,40,50]
for x in nums:
    if x==30:
        print("Found 30")
        break
    
    