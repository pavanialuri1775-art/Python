#Extract domain names
import re
s = "test@gmail.com hello@yahoo.in"
domains=re.findall(r"@([a-zA-Z0-9]+)\.",s)
print(domains)
