#palidrome
'''n=input("enter a number:")
rev=""
for ch in n:
    rev=ch+rev
if rev==n:
    print("palindrome")
else:
    print("not a palindrome")
    
#frequency of a each character
n=input("enter a string:")
freq={}
for ch in n:
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1
print(freq)'''

#find minimum
thelist=[23,34,25,12,16,18,17]
minimum=thelist[0]
for i in thelist:
    if i<minimum:
        minimum=i
print(minimum)
        
