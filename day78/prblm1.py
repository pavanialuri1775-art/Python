#Python Try Except
#The try block lets us  test a block of code for errors.
#The except block lets you handle the error.
#The else block lets you execute code when there is no error.
#The finally block lets us to execute code, regardless of the result of the try- and except blocks.

#Exception Handling
#When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
#These exceptions can be handled using the try statement.
#ex
#The try block will generate an exception, because x is not defined
#try:
  #print(x)
#except:
  #print("An exception occurred")
  

#Many Exceptions
#we can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error
#try:
  #print(x)
#except NameError:
  #print("Variable x is not defined")
#except:
  #print("Something else went wrong")


