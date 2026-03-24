#squares of a numbers
nums=[1,2,3,4,5]
square=[x*x for x in nums]
print(square)

#even numbers
nums=[1,2,3,4,5,6]
even_nums=[x for x in nums if x%2==0]
print(even_nums)

#convert to uppercase
words=["hello","world","python"]
new=[name.upper() for name in words]
print(new)

#length of each word.
words=["apple","pavani","pleasel"]
lengths=[len(name) for name in words]
print(lengths)

#filter numbers divisible by 3
nums=[1,2,3,4,5,6,7,8,9]
lst=[x for x in nums if x%3==0]
print(lst)

#replace negatives with 0
nums=[1,-2,3,-4,5]
result=[x if x>=0 else 0 for x in nums]
print(result)

#extract volwels
s="python programming"
vowels="AEIOUaeiou"
result=[ch for ch in s if ch in vowels ]
print(result)

#remove duplicates
nums=[1,2,3,1,2,3,5,5,6]
unique=list({x for x in nums})
print(unique)#[1, 2, 3, 5, 6]

#conditional expression
nums=[1,2,3,4,5]
even=[x for x in nums if x%2==0]
odd=[x for x in nums if x%2==1]
print("odd:",odd)#odd: [1, 3, 5]
print("even:",even)#even: [2,4]




  


                                                                                                                                                                                               
                                                                                                                                                                                               
                                                                                                                                                                                               
                                                                                                                                                                                               
                                                                                                                                                                                               
                                                                                                                                                                                               
                                                                                                                                                                                               