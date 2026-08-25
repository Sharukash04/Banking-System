from sortedcontainers import SortedDict

accounts_by_id=SortedDict()
accounts_by_balance=SortedDict()

def add_account(account):
    accounts_by_id[account.account_id]=account
    balance=account.get_balance()
    if balance not in accounts_by_balance:
        accounts_by_balance[balance]=[]
    accounts_by_balance[balance].append(account.account_id)

def get_accounts_by_id():
    return accounts_by_id.values()

def get_accounts_by_balance():
    result=[]
    for account_ids in accounts_by_balance.values():
        for account_id in account_ids:
            result.append(accounts_by_id[account_id])
    return result

def get_accounts_in_id_range(start_id,end_id):
    result=[]
    for account_id in accounts_by_id.irange(start_id,end_id):
        result.append(accounts_by_id[account_id])
    return result