from sortedcontainers import SortedDict


transactions=SortedDict()


def add_transaction(transaction):

    transactions[transaction.timestamp]=transaction


def get_transactions():

    return transactions.values()


def get_transactions_in_range(start_time,end_time):

    result=[]

    for timestamp in transactions.irange(
        minimum=start_time,
        maximum=end_time
    ):

        result.append(transactions[timestamp])

    return result