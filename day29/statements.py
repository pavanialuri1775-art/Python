#Python supports the usual logical conditions from mathematics
'''Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b'''
#we use these conditions in several ways most commonly in if statements
#if statement evaluates the condition and if the condition is true the code inside the if block is executed else If the condition is false, the code block is skipped.

#checking if a number is positive
number = 20
if number > 0:
  print("The number is positive")#The number is positive

#checking if b is greater than a
a = 33
b = 200
if b > a:
  print("b is greater than a")#b is greater than a
  
#if statement raises an error without indentation 
#Multiple Statements in If Block:we can have multiple statements inside a if block and all must be indented at same level.
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")
  
#using variables in conditions
#Boolean variables can be used directly in if statements without comparison operators
is_student=True
if is_student:
    print("i am a student")