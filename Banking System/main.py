from bank import (create_account, deposit, withdraw, get_balance, display_accounts, change_pin, close_account)

print("=" * 15 + " TN BANK " + "=" * 15)
print()
print()
print(" " * 10 + "WELCOME TO TN BANK")
print(" " * 5 + "Your trusted financial partner")
content = '''
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
    choice = int(input("Enter the number regarding to your choice: "))

    if choice == 1:
        account_id=input("Enter Account ID: ")
        while not account_id.isdigit() or int(account_id) <= 0:
            account_id=input("Enter Account ID (positive number): ")
        account_id=int(account_id)
        name=input("Enter Name: ")
        age=int(input("Enter Age: "))
        phone=input("Enter Phone Number (10 digits): ")
        while len(phone) !=10 or not phone.isdigit():
            phone=input("Enter Phone Number (10 digits): ")
            
        address=input("Enter Address: ")
        balance=float(input("Enter Opening Balance: "))
        
        pin=""
        while pin=="" or len(pin) !=4 or not pin.isdigit():
            pin=input("Enter 4-digit PIN: ")
            repin=input("Re-enter PIN: ")
            if pin!=repin:
                print("PINs do not match. Please try again.")
                pin=""

        if create_account(account_id, name, age, phone, address, balance, pin):
            print("Account created successfully!")
        else:
            print("Account ID already exists!")

    elif choice == 2:
        account_id=int(input("Enter Account ID: "))
        amount=float(input("Enter Amount to Deposit: "))
        if deposit(account_id, amount):
            print("Deposit successful!")
        else:
            print("Account not found!")

    elif choice == 3:
        account_id=int(input("Enter Account ID: "))
<<<<<<< HEAD
        amount=float(input("Enter Amount to withdraw:"))
        from bank import withdraw
        withdraw(account_id, amount)
    elif choice==4:
        account_id=int(input("Enter Account ID: "))
        from bank import get_balance
        balance=get_balance(account_id)
        print("Your Balance is:",balance)
    elif choice==5:
        from bank import display_accounts
        display_accounts()
    
=======
        amount=float(input("Enter Amount to withdraw: "))
        if withdraw(account_id, amount):
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    elif choice==4:
        account_id=int(input("Enter Account ID: "))
        balance=get_balance(account_id)
        if balance is not None:  #Check for None
            print("Your Balance is:",balance)
        else:
            print("Account not found!")

    elif choice==5:
        display_accounts()

    elif choice==6:
        account_id=int(input("Enter Account ID: "))
        old_pin=input("Enter Old PIN: ")
        new_pin=input("Enter New PIN: ")
        if change_pin(account_id,old_pin,new_pin):
            print("PIN changed successfully.")
        else:
            print("Invalid Account ID or PIN.")

    elif choice==7:
        account_id=int(input("Enter Account ID: "))
        pin = input("Enter PIN: ")
        if close_account(account_id, pin):
            print("Account closed successfully.")
        else:
            print("Invalid Account ID or PIN.")

    elif choice==8:
        print("Thank you for banking with us!")
        break
>>>>>>> c15adfd (completing the bank system project)
