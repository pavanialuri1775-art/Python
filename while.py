#A while loop runs as long as the condition is true.
#1 print 1 to 5
'''i=1  #starting value
while i<=5:  #loop runs while i<=5
    print(i)
    i+=1 #increases the value
    
#2 print even numbers
i=2
while i<=10:
    print(i)
    i+=2
    
#3 sum of numbers
n=int(input("enter a number:"))#5
i=1
total=0
while i<=n:
    total+=i
    i+=1
print(total)#15'''

#4 print numbers from 10 to 1
i=10
while i>=1:
    print(i)
    i-=1
    
#5 multiplication table
n=int(input("enter a number:"))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1
    