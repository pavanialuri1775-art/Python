#ATM Withdrawal
try:
    total_amount=int(input("enter amount:"))
    with_drawal=int(input("enter amount:"))
    if with_drawal>total_amount:
            raise ValueError("Insufficient Balance")
    print("Remaining Balance:",total_amount-with_drawal)
except ValueError as e:
    print(e)
    
#Bank PIN Validation
try:
    pin=int(input("enter pin:"))
    if pin==1234:
        print("Valid Pin")
    else:
        raise ValueError("Wrong PIN")
except ValueError as e:
    print(e)