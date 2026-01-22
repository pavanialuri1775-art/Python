#problems on int
a=5
b=3
print(a+b) #additon
print(a-b) #sub
print(a*b) #mul
print(a%b) #modulus(remainder)
print(a/b) #division(quotient)
print(a//b) #floor division(integer of quotient)

#square of a number
a=9
print(a**2)
 
#average of nunbers
a=24
b=40
print((a+b)/2)

#printing absolute value
x=-10
print(abs(x)) #abs() function returns the absolute value of a number
 
#adding 2 float numbers
a=25.6
b=27.8
print(a+b)

#Rounding a float to 2 decimal points
num=28.723
print(round(num,2))

#printing simple interest
P=float(input("Enter principal amount:"))
R=float(input("Enter rate of interest:"))
T=float(input("Enter time in years:"))
SI=(P*R*T)/100
print("simple interest:",SI)

#converting percentage to float
percentage=float(input("Enter Percentage:"))
decimal=percentage/100
print("float value is:",decimal)

#printing a complex number
num=2+3j
print(num)

#print real part of a complex number
z=3+4j
print(z.real) #.real attribute is used 

#creating a complex function using complex()
z=complex(5,7)
print(z)

#print imaginary part of a complex number
z=3+4j
print(z.imag) #.imag attribute is used.

#adding 2 complex numbers
z1=3+4j
z2=5+2j
sum=z1+z2
print("sum of complex numbers:",sum)
 
#checking type of a complex number
z=3+4j
print(type(z))











