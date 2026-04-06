#1
'''def count_even(nums):
    even_count=0
    for num in nums:
        if num%2==0:
            even_count+=1
    return even_count
my_list=[1,2,3,4,6]
print(count_even(my_list))

#2 first non repeating character
def first_non_repeating_char(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    for ch in s:
        if freq[ch]==1:
            return ch
    return -1
print(first_non_repeating_char("aabbcde"))'''

#3
def is_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    d={}
    for ch in s1:
        if ch in d:
            d[ch]=d[ch]+1
        else:
            d[ch]=1
    for ch in s2:
        if ch not in d:
            return False
        d[ch]-=1
        if d[ch]<0:
            return False
    return True
print(is_anagram("hello", "world"))
        