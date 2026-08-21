from storage import accounts
from collections import defaultdict
customer_index=defaultdict(list)
def add_account(account):
    accounts[account.account_id]=account
    customer_index[account.name].append(account.account_id)
    return True

def find_account(account_id):
    return accounts.get(account_id)

def account_exists(account_id):
    return account_id in accounts

def get_all_accounts():
    return accounts.values()

def delete_account(account_id):
    if account_id in accounts:
        account=accounts[account_id]
        del accounts[account_id]
        if account.name in customer_index:
            if account_id in customer_index[account.name]:
                customer_index[account.name].remove(account_id)
            if not customer_index[account.name]:
                del customer_index[account.name]
        return True
    return False

def find_accounts_by_name(name):
    account_ids=customer_index.get(name,[])
    result=[]

    for account_id in account_ids:
        account=accounts.get(account_id)
        if account:
            result.append(account)
    return result