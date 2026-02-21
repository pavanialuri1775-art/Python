#The range() function returns a sequence of numbers mostly used inside the loops.
#basic syntax:range(start,stop,step)
#start->starting number(default=0)
#stop->ending number(not included)
#step->gap between numbers(default=1)

#example
for num in range(5):
    print(num)#starts from 0 and ends at 4
    
#with start and stop
for num in range(2,6):
    print(num)#starts from 2 and ends at 5
    
#with step value
for i in range(1,9,2):
    print(i)#print odd numbers upto 7
    
#reverse range
for i in range(10,1,-1):
    print(i) #starts at 10 and ends at 2
    
#coverting a range to a list
numbers=list(range(1,6))
print(numbers)



