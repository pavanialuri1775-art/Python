#Else:
#we can use the else keyword define a block of code to be executed if no errors were raised.
#In this example, the try block does not generate any error.
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
#Finally
#The finally block, if specified, will be executed regardless if the try block raises an error or not
# 
try:
  #print(x)
#except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")