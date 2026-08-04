from storage import accounts
from account import Account


def create_account(account_id, name, age, phone, address, balance, pin):# Check duplicate account ID 
    for account in accounts:
        if account.account_id == account_id:
            return False  # Account already in bank
    
    account = Account(account_id,name,age,phone,address,balance,pin)
    accounts[account.account_id]=account
    return True

def find_account(account_id):
    if account_id in accounts:
        return accounts.get(account_id)
    return None

def deposit(account_id, amount):
    if account_id in accounts:
        accounts[account_id].deposit(amount)
        return True
    return False

def withdraw(account_id, amount):
    account=find_account(account_id)
    if account:
        return account.withdraw(amount)
    return False

def get_balance(account_id):
    account=find_account(account_id)
    if account:
        return account.get_balance()
    return None 

def display_accounts():
<<<<<<< HEAD
    for account in accounts:
        if account:
            print("ID:",account.account_id,"\n"
                  "| Name:",account.name,"\n"
                  "| Balance:",account.get_balance())
        else:
            print("No accounts found.")
=======
    if not accounts:
        print("No accounts found.")
    else:
        for account in accounts:
            print("| ID:", account.account_id, "\n" "| Name:", account.name, "\n" "| Balance:", account.get_balance())
            print("-" * 30)

def change_pin(account_id, old_pin, new_pin): #to pin change
    account = find_account(account_id)
    if account:
        return account.change_pin(old_pin, new_pin)
    return False

def close_account(account_id, pin): # to close account
    account = find_account(account_id)
    if account and account.verify_pin(pin):
        accounts.remove(account)
        return True
    return False
>>>>>>> c15adfd (completing the bank system project)
