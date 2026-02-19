#pass:The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.
#Why Use pass:
#when we are creating code structure but havent implemented the logic yet.
#when a statement is required syntactically but no action is needed.
#in empty functions or classses that we plan to implement later.

#pass in development:to sketch out the program before implementing the details.
#The pass statement allows us to do this without syntax errors.
#the pass is a null operation-nothing happens when it executes.it serves as a place holder.

#example:
a = 33
b = 200
if b > a:
  pass

#we can use pass in any branch of an if-elif-else statement.
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass #no action needed
else:
  print("Positive value")
  
#pass statement is also used in loops,functions and classes.
#Using pass with functions:
def calculate_discount(price):
      pass 

