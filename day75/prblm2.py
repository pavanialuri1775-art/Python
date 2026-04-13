#3 count vowels using regex
import re
s = "programming"
vowels=re.findall(r'[aeiou]',s)
print(len(vowels))

#4 Replace all spaces with '_'
import re
s = "hello world python"
r=re.sub(r'\s',"_",s)
print(r)

#5 Extract numbers from string
import re
s = "I have 2 apples and 10 bananas"
r=re.findall("\d+",s)
print(r)

#6 Validate mobile number (10 digits)
import re
s = "9876543210"
if re.fullmatch("\d{10}",s):
    print(True)
else:
    print(False)
    
#7 Remove special characters
import re
s = "a@b#c$123"
res=re.sub(r"[^a-zA-Z0-9]","",s)
print(res)
