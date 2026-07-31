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
        from Register import register
        register()
       

    elif choice == 2:
        from login import login
        login()