#global scope
#A variable created in the main body of the Python code is a global variable and belongs to the global scope
#Global variables are available from within any scope, global and local.
#example
x=300
def myfun():
    print(x)
myfun()
print(x)

#naming variables:if we operate with the same variable name inside and outside of a function,
#python will treat them as a separate variables ,one as global variable and other as local
#ex
x = 300
def myfunc():
  x = 200
  print(x)#200
myfunc()
print(x)#300

#global keyword:The global keyword makes the variable global.
#if we use global keyword,the variable belongs to the global scope.
def myfunc():
      global x
      x = 300
myfunc()
print(x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword.
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)#200









