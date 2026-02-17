#logical operators:used to combine conditional statements.
#and:Returns True if both statements are True
#or :Returns True if one of the statement is true
#not:Reverses the result

#and
a=200
b=30
c=45
if a>b and a>c:
    print("a is greater")
    
#or
a=200
b=30
c=250
if a>b or a>c:
    print("At least one condition is True")
    
#not
a=33
b=63
if not a>b:
    print("a is not greater than b")