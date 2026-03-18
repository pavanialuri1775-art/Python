#10
def unique_values(*args):
    unique=[]
    for num in args:
        if num not in unique:
            unique.append(num)
    return unique
print(unique_values(1,2,2,3,4,4))

#11
def filter_data(*args,**kwargs):
    filtered_list=[]
    min_value=kwargs.get("min")
    max_value=kwargs.get("max")
    for num in args:
        if min_value is not None and num<min_value:
            continue
        if max_value is not None and num>max_value:
            continue
        filtered_list.append(num)
    return filtered_list
print(filter_data(1,5,10,15,min=5)) 

#11 
def analyze(*args,**kwargs):
    sum=0
    count=0
    even_count=0
    for  num  in args:
        sum+=num
        count+=1
        if num%2==0:
            even_count+=1
        
    return {"sum":sum,"count":count,"even":even_count}
print(analyze(1,2,3,4))
    