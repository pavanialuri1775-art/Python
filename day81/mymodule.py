#Module:A file that containing set of functions we want to include in our application.
#creating  module 
#creating file 
#mymodule.py
#inside file:
def greeting(name):
    print("Hello", name)
    
#Use Module
#another file:
import mymodule
mymodule.greeting("pavani")

#variables in module
name="pavani"
age=22
import mymodule
print(mymodule.name)
print(mymodule.age)

#import with alias
#Use as 
import mymodule as mx
print(mx.name)