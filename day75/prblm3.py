#8 Extract emails
import re
s = "test@gmail.com hello@yahoo.com"
x=re.findall(r"[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",s)
print(x)


