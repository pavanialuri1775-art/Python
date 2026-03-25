#use of lambda functions
#we have a function that takes one argument,and that argument  will be multiplied with an unknown number
def myfun(n):
    return lambda a:a*n
#Use that function definition to make a function that always doubles the number you send in.
def myfun(n):
    return lambda a:a*n
mydoubler=myfun(2)
print(mydoubler(22))#44
#we can use same function definition to make a func that always triples the num
def myfun(n):
    return lambda a:a*n
mytripler=myfun(3)
print(mytripler(11))

#we can also use the same func to make both functions.
def myfunc(n):
      return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(12))#24
print(mytripler(12))#36


