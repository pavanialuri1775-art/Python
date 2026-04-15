#add 
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a%b
n,m=map(int,input("").split())

print("Add:",add(n,m))
print("sub:",sub(n,m))
print("mul:",mul(n,m))
print("div:",div(n,m))