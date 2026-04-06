#
def sum_of_digits(n):
    total=0
    m=str(n)
    for i in m:
        total+=int(i)
    return total
print(sum_of_digits(1234))

#count vowels
def count_vowels(s):
    count=0
    vowels="AEIOUaeiou"
    for ch in s:
        if ch in vowels:
            count+=1
    return count
print(count_vowels("pavani"))

#second largest
def second_largest(arr):
    arr.sort()
    return arr[-2]
my_list=[4,7,2,6,8]
print(second_largest(my_list))

#
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(is_prime(9))

#reverse words
def reverse_words(s):
    words=s.split()
    result=[]
    for word in words:
        result.append(word[::-1])
    return " ".join(result)
print(reverse_words("I am pavani"))

#remove duplicates
def remove_duplicates(arr):
    result=[]
    for num in arr:
        if num not in result:
            result.append(num)
    return result
my_arr=[1,2,2,3,1]
print(remove_duplicates(my_arr))

