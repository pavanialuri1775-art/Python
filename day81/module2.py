#Example
import math
print(math.sqrt(25))

#
import random
print(random.randint(1,10))

#dir() Function:Shows all names inside module.
import math
print(dir(math))

#Import Specific Item:instead of full module
from math import sqrt
print(sqrt(100))


#Multiple imports 
from math import sqrt,factorial
print(sqrt(16))
print(factorial(5))

