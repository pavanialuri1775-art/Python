#Remove duplicate spaces
import re
s = "hello   world   python"
duplicates=re.sub(r"\s+"," ",s)
print(duplicates)

#Extract hashtags
import re
s = "Learning #python #regex is fun"
hashtags=re.findall(r"#[a-zA-z]+",s)
print(hashtags)

#Validate 
import re
s = "user_123"
if re.fullmatch(r'[a-zA-Z0-9_]{5,15}',s):
    print(True)
else:
    print(False)


