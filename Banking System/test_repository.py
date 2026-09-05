from account import Account
from json_account_repository import JsonAccountRepository


repository=JsonAccountRepository()


account=Account(
    102,
    "Test User",
    20,
    "9876543211",
    "Trichy",
    3000,
    "5678"
)


repository.save(account)

print("Account saved")

found_account=repository.get(102)

if found_account:
    print("Account found:",found_account.name)
    print("Balance:",found_account.get_balance())

accounts=repository.list()

print("Total accounts:",len(accounts))

deleted=repository.delete(102)

print("Account deleted:",deleted)

found_account=repository.get(102)

print("Account after delete:",found_account)