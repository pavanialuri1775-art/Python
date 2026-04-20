#1 list index error
a = [10, 20, 30]
try:
    n=int(input("enter index:"))
    print(a[n])
except IndexError:
    print("invalid index")
    
#2 Dictionary Key Error
d = {"name": "Ram", "age": 22}
try:
    n=input("enter key:")
    print(d[n])
except KeyError:
    print("key not found")
    
#3 
try:
    f=open("data.txt")
    print(f.read())
except FileNotFoundError:
    print("File not found")
    
