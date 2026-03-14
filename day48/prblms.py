#for the given list of strings find a str which is a palindromic string
thelist=["pavani","afifa","lavss","madam","racecar"]
for word in thelist:
    if word==word[::-1]:
        print(word)


#take a list str and cnt the vowels in each str,  if the cnt of vowels is even print the str
thelist=["apple","pavss","banana","durga"]
for word in thelist:
    vowels="AEIOUaeiou"
    count=0
    for ch in word:
        if ch in vowels:
            count+=1
    if count%2==0:
        print(word)
        
    
        
