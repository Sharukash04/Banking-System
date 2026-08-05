from storage import accounts
from account import Account

#Create new account with unique ID
def create_account(acc_id,name,age,phone,address,balance,pin):
    if acc_id in accounts:
        return False
    acc=Account(acc_id,name,age,phone,address,balance,pin)
    accounts[acc_id]=acc
    return True

#Find account using dictionary key lookup
def find_account(acc_id):
    return accounts.get(acc_id)

#Add money to existing account
def deposit(acc_id,amount):
    acc=accounts.get(acc_id)
    if acc:
        acc.deposit(amount)
        return True
    return False

#Withdraw money from account
def withdraw(acc_id,amount):
    acc=accounts.get(acc_id)
    if acc:
        return acc.withdraw(amount)
    return False

#Get account balance
def get_balance(acc_id):
    acc=find_account(acc_id)
    if acc:
        return acc.get_balance()
    return None

#Display all accounts in bank
def display_accounts():
    if not accounts:
        print("No accounts in bank")
        return
    print("\n========== BANK ACCOUNTS ==========")
    print("ID    Name           Balance")
    print("-----------------------------------")
    for acc_id,acc in accounts.items():
        print(f"{acc_id:<6}{acc.name:<15}{acc.get_balance():.2f}")
    print("===================================\n")

#Change account PIN after verification
def change_pin(acc_id,old_pin,new_pin):
    acc=find_account(acc_id)
    if acc:
        return acc.change_pin(old_pin,new_pin)
    return False

#Remove account from bank
def close_account(acc_id,pin):
    acc=find_account(acc_id)
    if acc and acc.verify_pin(pin):
        del accounts[acc_id]
        return True
    return False