#Generators saves memory
#Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.
#For large datasets, generators save memory
#ex:
def large_sequence(n):
      for i in range(n):
        yield i
# This doesn't create a million numbers in memory       
gen = large_sequence(1000000)
print(next(gen))#0
print(next(gen))#1
print(next(gen))#2

#Using next() with Generators
#You can manually iterate through a generator using the next() function
def simple_gen():
      yield "Emil"
      yield "Tobias"
      yield "Linus"
gen = simple_gen()
print(next(gen))#Emil
print(next(gen))#tobias
print(next(gen))#linus
#When there are no more values to yield, the generator raises a StopIteration exception.
