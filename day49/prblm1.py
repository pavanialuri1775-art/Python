#1
i=1
while i<=10:
    if i==6:
        break
    print(i,end=" ")
    i+=1
    
#2
i=1
while i<=10:
    if i==5:
        i+=1
        continue
    print(i,end=" ")
    i+=1
    
#3
i=1
while i<=15:
    if i%4==0:
        i+=1
        continue
    if i==13:
        break
    print(i,end=" ")
    i+=1
    
    
    
