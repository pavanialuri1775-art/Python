#count even and odd numbers
lst=[1,2,3,4,5,6,7,8]
even_count=0
odd_count=0
for i in lst:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("evencount is:",even_count)#evencount is:4 
print("oddcount is:",odd_count)#oddcount is: 4

#frequency of a character
n=input("enter a string:")
freq={}
for ch in n:
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1
for key in freq:
    print(key,":",freq[key])
    
#removing duplicates using loop
lst=[1,2,2,3,4,5,4]
the_list=[]
for i in lst:
    if i not in the_list:
        the_list.append(i)
print(the_list)
        
        
        
    