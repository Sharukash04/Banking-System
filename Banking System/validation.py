from storage import accounts


def check_duplicate(account_id):

    for account in accounts:
        if account[0] == account_id:
            return True

    return False


def valid_amount(amount):

    if amount > 0:
        return True

    return False