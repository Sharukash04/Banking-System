from account import *
from validation import *


while True:

    print("\n===== BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Balance Check")
    print("5. Display Accounts")
    print("6. Exit")


    choice = input("Enter choice: ")


    if choice == "1":

        account_id = input("Enter Account ID: ")

        if check_duplicate(account_id):
            print("Account ID already exists")

        else:
            name = input("Enter Name: ")
            balance = float(input("Initial Deposit: "))

            create_account(account_id, name, balance)

            print("Account Created Successfully")


    elif choice == "2":

        account_id = input("Enter Account ID: ")
        amount = float(input("Deposit Amount: "))


        if valid_amount(amount):

            if deposit(account_id, amount):
                print("Deposit Successful")

            else:
                print("Account Not Found")

        else:
            print("Invalid Amount")


    elif choice == "3":

        account_id = input("Enter Account ID: ")
        amount = float(input("Withdraw Amount: "))


        if withdraw(account_id, amount):
            print("Withdrawal Successful")

        else:
            print("Withdrawal Failed")


    elif choice == "4":

        account_id = input("Enter Account ID: ")

        account = get_balance(account_id)


        if account:

            print("\nAccount Details")
            print("ID:", account[0])
            print("Name:", account[1])
            print("Balance:", account[2])

        else:
            print("Account Not Found")


    elif choice == "5":

        display_accounts()


    elif choice == "6":

        print("Thank you!")
        break


    else:

        print("Invalid Choice")