#check even or odd 
def even_or_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
m=int(input("enter a number:"))
print(even_or_odd(m))