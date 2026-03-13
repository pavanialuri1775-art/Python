#1
def fun(**data):
    print("hi i'm",data["name"],data["course"],data["branch"],"with",data["per"])
fun(name="pavani",course="btech",branch="CSM",per="80%")

#2
def prime_number(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
n=int(input("enter a number:"))
for i in range(2,n+1):
    if prime_number(i):
        print(i,end=" ")