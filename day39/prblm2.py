# frequnecy of a character in a string
n=input("enter a number:")
freq={}
for ch in n:
    freq[ch]=freq.get(ch,0)+1
print(freq)

