#raise Custom Exception:raise=creating error ourself
'''try:
    age=int(input("Enter age:"))
    if age<18:
        raise Exception("Not eligible")
    print("Eligible")
except Exception as e:
    print(e)'''
    
#Password Validation using raise
try:
    n=input("enter password:")
    if len(n)<8:
        raise ValueError("weak password")
    print("strong password")
except ValueError as e:
    print(e)