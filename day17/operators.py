'''n=int(input("enter an integer:"))
if n>0 and (n&(n-1))==0:
    print(True)
else:
    print(False) 

n=int(input("enter an integer"))
print(n>0 and (n&(n-1)))

#Take a number and left shift it by 2 positions.
n=int(input("enter a number:")) #4
print(n<<2) #16

#Check whether a number is odd using bitwise operator.
n=int(input("enter a number:")) #5
print(n&1==1) #odd num ends with 1 in binary so it returns True'''

#Check whether a number is even using bitwise operator.
n=int(input("enter a number:"))  #4
print(n & 1 == 0) #True
