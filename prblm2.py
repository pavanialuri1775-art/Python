#count digits
def count_digits(n):
    if n==0:
        return 0
    return 1+count_digits(n//10)
print(count_digits(1234))#4

#reverse string 
def reverse(s):
    if len(s)<=1:
        return s
    return reverse(s[1:])+s[0]
print(reverse("pavani"))#inavap


#check palindrome
def is_palindrome(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("afifa"))#True