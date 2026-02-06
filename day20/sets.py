#sets:An unordered collection of unique elements.
#no duplicates
#unordered(no indexing)
#sets are mutable
#elements inside a set are immutable
#sets are denoted with curly braces

#Creating Sets
a={1,2,3}
print(a) #{1,2,3}

#the set() constructor is used to make a set.
b=set([4,5,6]) 
print(b) #{4,5,6}

#No Duplicates
s={1,2,2,3,3}
print(s) #{1,2,3}

#type()
s={1,2,3,4,5}
print(type(s))

#Set items can be of any data type
#string,int and boolean
set1={"apple","banana","cherry"}
set2={1,5,7,9,3}
set3={True,False,False}
print(set1) #{'apple','cherry','banana'}
print(set2) #{1, 3, 5, 7, 9}
print(set3) #{False, True}

#A set can contain different data types
set1={"abc",34,True,40,"male"}
print(set1)#{True, 34, 40, 'abc', 'male'}









