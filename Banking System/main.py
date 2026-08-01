
print("="*15 + " TN BANK " + "="*15)
print()
print()
print(" "*10 +"WELCOME TO TN BANK")
print(" "*5+"Your trusted financial partner")
content='''
1. Create Account
2. Deposit
3. Withdraw
4. Balance Check
5. Display Accounts
6. Change PIN
7. Close Account
8. Exit'''
print()
while True:
    print(content)
    choice=int(input("Enter the number regarding to your choice:"))

    if choice == 1:
        account_id = int(input("Enter Account ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        phone = input("Enter Phone: ")
        address = input("Enter Address: ")
        balance = float(input("Enter Opening Balance: "))
        pin = input("Enter 4-digit PIN: ")

        from bank import create_account
        create_account(account_id,name,age,phone,address,balance,pin)

    elif choice==2:
        account_id=int(input("Enter Account ID: "))
        amount=float(input("Enter Amount to Deposit:"))
        from bank import deposit
        deposit(account_id, amount)

    elif choice==3:
        account_id=int(input("Enter Account ID: "))
        amount=float(input("Enter Amount to withdraw:"))
        from bank import withdraw
        withdraw(account_id, amount)