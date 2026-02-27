#prime numbers from 1 t0 n
n=int(input("enter a number:"))
if n<=1:
    print("not prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("prime")