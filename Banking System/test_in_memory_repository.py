from account import Account
from in_memory_account_repository import InMemoryAccountRepository


repository=InMemoryAccountRepository()


account=Account(
    301,
    "Memory Test",
    20,
    "9876543213",
    "Trichy",
    4000,
    "1234"
)


repository.save(account)

print("Account saved")

found_account=repository.get(301)

print("Account found:",found_account.name)
print("Balance:",found_account.balance)

accounts=repository.list()

print("Total accounts:",len(accounts))

deleted=repository.delete(301)

print("Account deleted:",deleted)

found_account=repository.get(301)

print("Account after delete:",found_account)