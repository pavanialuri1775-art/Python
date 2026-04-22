#numbers from 1 to 5
class Numbers:
    def __init__(self):
        self.x=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.x<=5:
            val=self.x
            self.x+=1
            return val
        else:
            raise StopIteration
obj=Numbers()
for i in obj:
    print(i)