#lamda:A lamda is a small,one line function without a name.
#syntax:
#lambda arguments:expression(can take any no of inputs but only in oneline)
#ex
x=lambda a:a+10
print(x(5))#15

#ex2
x=lambda a,b:a*b
print(x(3,4))#12

#ex3
x=lambda a,b,c:a+b+c
print(x(3,4,5))#12

#lambda is a shortcut for a function.
#lambda is used when we need a quick,small function for temporary use.
#lambda=quick function(one line only)

#ex4
f=lambda x:x*x
print(f(6))#36
