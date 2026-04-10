#
def my_fun(n):
    for i in range(n):
        if i%3==0:
            yield i
n=int(input())
for j in my_fun(n):
    print(j)
