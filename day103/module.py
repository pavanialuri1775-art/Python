#permutations means arranging items in different possible orders
#python already has permutation function
#python provides it through itertools module

from itertools import permutations
arr=[1,2,3,4]
for p in permutations(arr):
    print(p)
    
#if we want arrngements of only 2 elements
from itertools import permutations
arr=[1,2,3]
for p in permutations(arr,2):
    print(p)
