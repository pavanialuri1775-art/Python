#4 squares  generator
def square(n):
    for i in range(1,n+1):
        yield i*i
for num in square(4):
    print(num,end=" ")
    
#5 String Characters Generator
def character(s):
    for ch in s:
        yield ch
for ch in character("abc"):
    print(ch,end=" ")
    
#6 R+everse String Generator
def revers(s):
    rev=""
    for ch in s:
        rev=ch+rev
    yield rev
for ch in revers("pavani"):
    print(ch,end=" ")
    
    
    