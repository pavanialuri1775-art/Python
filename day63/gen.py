#Generators:Generators are functions that can pause and resume their execution.
#when a generator function is called,it returns a generator object.
#ex:A simple generator function.
def my_generator():
      yield 1
      yield 2
      yield 3
for value in my_generator():
  print(value)

#yield keyword:When yield is encountered, the function's state is saved, and the value is returned. 
#The next time the generator is called, it continues from where it left off.
def count_num(n):
    count=1
    while count<=n:
        yield count
        count+=1
for num in count_num(5):
    print(num)
#Unlike return, which terminates the function, yield pauses it and can be called multiple times.



