from storage import accounts
from account import Account


def create_account(account_id, name, age, phone, address, balance, pin):
    account = Account(
    account_id,
    name,
    age,
    phone,
    address,
    balance,
    pin
)
    accounts.append(account)
    return True

def find_account(account_id):
    for account in accounts:
        if account.account_id==account_id:
            return account
    return None

def deposit(account_id, amount):
    account=find_account(account_id)
    if account:
        account.deposit(amount)
        return True
    return False

def withdraw(account_id, amount):
    account=find_account(account_id)
    if account:
        return account.withdraw(amount)
    return False

def get_balance(account_id):
    account = find_account(account_id)
    return account.get_balance()

def display_accounts():
    for account in accounts:
        print("ID:", account.account_id,"| Name:",account.name,"| Balance:",account.get_balance()        )