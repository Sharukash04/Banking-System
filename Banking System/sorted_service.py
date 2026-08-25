import bisect
account_ids=[]

def add_account(account_id):
    bisect.insort(account_ids,account_id)

def get_account_ids():
    return account_ids

def get_ids_in_range(start_id,end_id):
    start_index=bisect.bisect_left(account_ids,start_id)
    end_index=bisect.bisect_right(account_ids,end_id)
    return account_ids[start_index:end_index]