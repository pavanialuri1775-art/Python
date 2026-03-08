#while loop:With the while loop we can execute a set of statements as long as a condition is true.
#example
i=1
while i<6:
    print(i)
    i+=1
#Note: remember to increment i, or else the loop will continue forever.

#break statement:With the break statement we can stop the loop even if the while condition is true
#break when i=2
i=1
while i<6:
    print(i)
    if i==2:
        break
    i+=1
    
#continue statement:with the continue statement we can stop the current iteration and continue the next.
i=1
while i<8:
    i+=1
    if i==4:
        continue
    print(i)



