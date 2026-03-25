#sort list of tuples by second value.
lst=[(1,5),(2,3),(4,5)]
new_lst=sorted(lst,key=lambda x:x[1])
print(new_lst)

#sort words based on the length
words=["pavsss","geethzzz","avnshhh","keertzzz"]
new_lst=sorted(words,key=lambda x:len(x))
print(new_lst)##['pavsss', 'avnshhh', 'geethzzz', 'keertzzz']

#square only even numbers
nums=[1,2,3,4,5,6]
even_nums=filter(lambda x:x%2==0,nums)
squares=list(map(lambda x:x**2,even_nums))
print(squares)#[4, 16, 36]

#
nums=list(range(1,21))
new_lst=filter(lambda x:x%2==0,nums)
multiply=list(map(lambda x:x*10,new_lst))
print(multiply)#[20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
    



