from bank import create_account,deposit,withdraw,get_balance,display_accounts,change_pin,close_account

print("="*15+" TN BANK "+"="*15)
print()
print()
print(" "*10+"WELCOME TO TN BANK")
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
    choice=int(input("Enter your choice: "))

    if choice==1:
        #Get valid account ID
        while True:
            acc_id=input("Enter Account ID (+ve number): ")
            if acc_id.isdigit() and int(acc_id)>0:
                acc_id=int(acc_id)
                break
            print("Invalid ID. Please enter positive number")

        name=input("Enter Name: ")

        #Get valid age
        while True:
            age=input("Enter Age: ")
            if age.isdigit() and int(age)>0:
                age=int(age)
                break
            print("Invalid age. Please enter positive number")

        #Get valid phone number
        while True:
            phone=input("Enter Phone Number (10 digits): ")
            if len(phone)==10 and phone.isdigit():
                break
            print("Phone must be exactly 10 digits")

        address=input("Enter Address: ")

        #Get valid opening balance
        while True:
            balance=input("Enter Opening Balance: ")
            if balance.replace('.','').isdigit() and float(balance)>=0:
                balance=float(balance)
                break
            print("Invalid balance. Please enter positive number")

        #Get and confirm PIN
        while True:
            pin=input("Enter 4-digit PIN: ")
            if len(pin)==4 and pin.isdigit():
                repin=input("Re-enter PIN: ")
                if pin==repin:
                    break
                print("PINs do not match. Try again")
            else:
                print("PIN must be exactly 4 digits")

        if create_account(acc_id,name,age,phone,address,balance,pin):
            print("Account created successfully")
        else:
            print("Account ID already exists")

    elif choice==2:
        acc_id=int(input("Enter Account ID: "))
        amount=float(input("Enter Amount to Deposit: "))
        if deposit(acc_id,amount):
            print("Deposit successful")
        else:
            print("Account not found")

    elif choice==3:
        acc_id=int(input("Enter Account ID: "))
        amount=float(input("Enter Amount to Withdraw: "))
        if withdraw(acc_id,amount):
            print("Withdrawal successful")
        else:
            print("Insufficient balance or account not found")

    elif choice==4:
        acc_id=int(input("Enter Account ID: "))
        balance=get_balance(acc_id)
        if balance is not None:
            print(f"Your Balance is: {balance:.2f}")
        else:
            print("Account not found")

    elif choice==5:
        display_accounts()

    elif choice==6:
        acc_id=int(input("Enter Account ID: "))
        old_pin=input("Enter Old PIN: ")
        new_pin=input("Enter New PIN: ")
        if change_pin(acc_id,old_pin,new_pin):
            print("PIN changed successfully")
        else:
            print("Invalid Account ID or PIN")

    elif choice==7:
        acc_id=int(input("Enter Account ID: "))
        pin=input("Enter PIN: ")
        if close_account(acc_id,pin):
            print("Account closed successfully")
        else:
            print("Invalid Account ID or PIN")

    elif choice==8:
        print("Thank you for banking with us")
        break

    else:
        print("Invalid choice. Enter number between 1 and 8")