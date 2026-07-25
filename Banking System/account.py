from storage import accounts


def create_account(account_id, name, balance):
    accounts.append([account_id, name, balance])
    return True


def find_account(account_id):
    for account in accounts:
        if account[0] == account_id:
            return account

    return None


def deposit(account_id, amount):
    account = find_account(account_id)

    if account:
        account[2] = account[2] + amount
        return True

    return False


def withdraw(account_id, amount):
    account = find_account(account_id)

    if account:
        if amount <= account[2]:
            account[2] = account[2] - amount
            return True

    return False


def get_balance(account_id):
    account = find_account(account_id)

    if account:
        return account

    return None


def display_accounts():
    for account in accounts:
        print(
            "ID:",
            account[0],
            "| Name:",
            account[1],
            "| Balance:",
            account[2]
        )