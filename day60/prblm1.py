#multiply each  num by 3
nums=[1,2,3,4]
new_lst=list(map(lambda x:x*3,nums))
print(new_lst)#[3, 6, 9, 12]

#Add 5 to each element
nums=[10,20,30]
new_lst=list(map(lambda x:x+5,nums))
print(new_lst)#[15,25,35]

#get only numbers divisile by 3
nums=[3,5,6,9,10,12]
new_lst=list(filter(lambda x:x%3==0,nums))
print(new_lst)#[3, 6, 9, 12]

#get numbers less than 10
nums=[5,12,7,18,3]
new_lst=list(filter(lambda x:x<10,nums))
print(new_lst)[5,7,3]

