#Generator Methods
#1:send() Method:The send() method allows you to send a value to the generator.
def echo_generator():
      while True:
        received = yield
        print("Received:", received)
gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")#Received: Hello
gen.send("World")#Received: World

#close method:The close() method stops the generator
def my_gen():
    try:
      yield 1
      yield 2
      yield 3
    finally:
     print("Generator closed")
gen = my_gen()
print(next(gen))#1
gen.close()