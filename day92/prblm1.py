#Character Frequency
'''name=input("Enter a string:")
freq={}
for ch in name:
    freq[ch]=freq.get(ch,0)+1
print(freq)
    
#Word Analyzer
sentence=input("enter a sentence:")
s=sentence.split()
print("Total words:",len(s))
s.sort(key=len)
print("Longest word:",s[-1])
print("shortest word:",s[0])'''

#Password Validator
password=input("Enter a password:")
has_upper=False
has_digit=False
for ch in password:
    if ch.isupper():
        has_upper=True
    if ch.isdigit():
        has_digit=True
if len(password) >= 8 and has_upper and has_digit:
    print("Valid Password")
    if len(password) < 8:
        print("Password must contain at least 8 characters")
    if not has_upper:
        print("Password must contain at least one uppercase letter")
    if not has_digit:
        print("Password must contain at least one digit")