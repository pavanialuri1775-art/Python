#4
def count_words(s):
    word=s.split()
    return len(word)
print(count_words("I am pavani"))

#Missing number
def missing_number(arr,n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total-sum(arr)
my_list=[1,2,4,5]
print(missing_number(my_list,5))
        