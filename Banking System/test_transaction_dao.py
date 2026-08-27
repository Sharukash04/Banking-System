from transaction import Transaction
import transaction_dao
from datetime import datetime


transaction1=Transaction(
    "DEPOSIT",
    1000,
    101,
    101,
    datetime(2026,8,20,10,30)
)

transaction2=Transaction(
    "WITHDRAW",
    500,
    101,
    101,
    datetime(2026,8,22,12,30)
)

transaction3=Transaction(
    "DEPOSIT",
    2000,
    101,
    101,
    datetime(2026,8,21,9,30)
)


transaction_dao.add_transaction(transaction1)
transaction_dao.add_transaction(transaction2)
transaction_dao.add_transaction(transaction3)


print("All transactions:")

for transaction in transaction_dao.get_transactions():

    print(
        transaction.timestamp,
        transaction.transaction_type,
        transaction.amount
    )


print("\nTransactions from 2026-08-20 to 2026-08-21:")

start_time=datetime(2026,8,20,0,0)
end_time=datetime(2026,8,21,23,59,59)

result=transaction_dao.get_transactions_in_range(
    start_time,
    end_time
)

for transaction in result:

    print(
        transaction.timestamp,
        transaction.transaction_type,
        transaction.amount
    )