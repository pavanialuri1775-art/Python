#
def dec(func):
    def wrap():
        print(func()*2)
    return wrap
@dec
def func():
    return int(input())
func()