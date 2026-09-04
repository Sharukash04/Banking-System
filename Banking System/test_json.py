from account import Account
from transaction import Transaction
from json_storage import save_accounts,load_accounts
from datetime import datetime


account=Account(
    101,
    "Sharukash",
    19,
    "9876543210",
    "Trichy",
    5000,
    "1234"
)


transaction=Transaction(
    "DEPOSIT",
    1000,
    101,
    101,
    datetime.now()
)


account.transactions.append(transaction)

accounts=[account]

save_accounts(accounts)

print("Account and transaction saved successfully")

loaded_accounts=load_accounts()

print(loaded_accounts)