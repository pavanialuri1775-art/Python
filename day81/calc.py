#Create Calculator module
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
 
import calc
print(calc.add(10,5))

#datetime:used for date and time.
import datetime
now=datetime.datetime.now()
print(now)
print(now.year)
print(now.month)

#calendar:used to print calendars
import calendar
print(calendar.month(2026,4))#monthly calendar display

#os :used to interact with operating system
import os
print(os.getcwd())#current folder

#sys:used for system level features
import sys
print(sys.version)

#re(regular expresion)
import re
s="abc123"
print(re.findall(r'\d',s))

#collections
#counter
from collections import Counter
print(Counter("banana"))

#deque
from collections import deque
d = deque([1,2,3])
d.appendleft(0)
print(d)

#heapq:Used for min heap / priority queue.
import heapq
a = [5,2,8,1]
heapq.heapify(a)
print(heapq.heappop(a))
