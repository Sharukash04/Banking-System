from storage import accounts


def add_account(account):
    accounts[account.account_id] = account
    return True


def find_account(account_id):
    return accounts.get(account_id)


def account_exists(account_id):
    return account_id in accounts


def get_all_accounts():
    return accounts.values()


def delete_account(account_id):
    if account_id in accounts:
        del accounts[account_id]
        return True

    return False