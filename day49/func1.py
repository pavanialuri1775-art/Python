#function:A function is a block of code that performs a specific task  and can be called whenever needed
#EXAMPLE
def function_name(parameters):
    #code block
    return
#def keyword is used to define a keyword
#function_name:our function_nmae(meaningful names)
#parameters-input values
#return-sends a value back

#simple example
def greet():
    print("Hello, Pavani!")
greet()

#functions with parameters
def greet_person(name):
    print(f'hello,{name}!')
greet_person("pavani")
greet_person("pavss")

#functions with return values
def add(a,b):
    return a+b
result=add(5,8)
print(result)