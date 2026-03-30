#11
def analyze(*args, **kwargs):
    print("sum:",sum(args)) 
    print("max:",max(args))
    for key,value in kwargs.items():
        print(key,":",value)
analyze(2,5,1,name="Pavani")  

#12
#using return
def analyze(*args,**kwargs):
    result={}     
    if args:
        result["sum"]=sum(args)  
        result["max"]=max(args)    
    result["details"]=kwargs
    return result
print(analyze(2,5,1,name="Pavani"))     