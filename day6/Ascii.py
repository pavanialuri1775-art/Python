#to print ASCII value of an character we use ord()
ch = 'A'
print(ord(ch)) #65

#Character from ASCII value
print(chr(97)) #a

#we use abs() to find the absolute difference between two characters
ch1 = 'a'
ch2 = 'd'
print(abs(ord(ch1) - ord(ch2)))

ch="d"
print(ch.isupper())
print(ch.islower())

#Convert lowercase → uppercase
ch="g"
print(ch.upper())

#Palindrome:a palindrome is a word,number,or string that reads the same forward and backward.
s="pavani"
print(s==s[::-1])




