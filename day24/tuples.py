#count()
t=(1,2,3,4,5,2,4,5)
print(t.count(2))

#index()
t=("apple","banana","cherry","banana")
print(t.index("banana"))

#check element
t=(10, 20, 30, 40)
if 20 in t:
    print("True")
    
#Length of Tuple
t=(5,10,15,20,25)
print(len(t))

#Find Maximum & Minimum
t = (12, 45, 7, 89, 23)
print(max(t))
print(min(t))

#Convert List to Tuple
l=[1, 2, 3, 4, 5]
k=tuple(l)
print(k)

#Tuple Concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1+t2)

#Count Multiple Elements
t = (1, 2, 2, 3, 3, 3, 4)
print(t.count(1))
print(t.count(2))

#Tuple Unpacking
t = (100, 200, 300)
a,d,f=t
print(a)
print(d)
print(f)