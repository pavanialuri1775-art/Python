#Extract only alphabets
import re
s = "abc123XYZ@#"
x="".join(re.findall(r"[a-zA-Z]+",s))
print(x)

#2. Extract all numbers (continuous)
import re
s = "ab12cd345ef6"
x=re.findall("\d+",s)
print(x)

#3 Find words starting with vowel
import re
s = "apple banana orange umbrella cat"
x=re.findall(r"\b[aeiouAEIOU][a-zA-Z]*",s)
print(x)


