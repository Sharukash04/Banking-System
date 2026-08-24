import bisect


account_ids=[]


def add_account_id(account_id):

    bisect.insort(account_ids,account_id)


def get_account_ids():

    return account_ids