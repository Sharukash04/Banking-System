from account import Account
from transaction import Transaction
from json_storage import save_all,load_accounts
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


save_all(accounts)

print("Account saved successfully")


loaded_accounts=load_accounts()

loaded_account=loaded_accounts[0]

print("Loaded account:",loaded_account.name)
print("Loaded balance:",loaded_account.get_balance())
print("Loaded transactions:",len(loaded_account.transactions))


print(
    "Transaction type:",
    loaded_account.transactions[0].transaction_type
)


print(
    "Transaction amount:",
    loaded_account.transactions[0].amount
)


print(
    "Transaction timestamp:",
    loaded_account.transactions[0].timestamp
)