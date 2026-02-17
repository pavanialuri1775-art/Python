#The Elif Keyword
#it is used to check multiple conditions one after the other.
#python checks if the if condition first
#if it is False,it checks the elif condition and execute a block of code as soon as one of the condition evaluates True
#example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")#a and b are equal
  
#Multiple Elif Statements
#we can have many elif statements as we need.python will check each condition in order and execute the first one that is true
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 50:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")#Grade: C
  #the program checks each condition in order and prints the first condition that evaluates to True
  #Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.

#we use elif when we have multiple conditions to check.it is more efficient than
#using multiple seperate if statements.