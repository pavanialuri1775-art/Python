#ATM Withdraw System
#Take balance and withdraw amount.
try:
    amount=int(input("Enter balance amount:"))
    withdraw_amount=int(input("Enter withdraw amount:"))
    if withdraw_amount>amount:
        raise ValueError("insufficient balance")
    elif amount<=0:
        raise ValueError("Insufficient balance")
    amount=amount-withdraw_amount
    print("withdraw succesfull")
    print("remaining amount:",amount)
except ValueError as e:
    print(e)