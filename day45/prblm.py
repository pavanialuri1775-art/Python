#reversing a number
num = input("Enter a number: ")
rev = ""
for i in num:
    rev = i + rev
print("Reversed number:", rev)

#Print elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i)
    
#Calculate the cube of all numbers from 1 to a given number
n=int(input("enter a number:"))
for i in range(1,n+1):
       print(i**3)
       
#Print Full Multiplication Table
n=int(input("enter a number:"))#3
for i in range(1,11):
    print(i*n,end=" ")#3 6 9 12 15 18 21 24 27 30 
