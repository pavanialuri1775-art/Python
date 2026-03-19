#Scope
#A variable is only available from inside the region it is created. This is called scope.
#local Scope:A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
#example
def myfunc():
      x = 300
      print(x)#300
myfunc()

#function inside Function
#The local variable can be accessed from a function within the function
def myfunc():
      x = 300
      def myinnerfunc():
        print(x)
      myinnerfunc()
myfunc()







