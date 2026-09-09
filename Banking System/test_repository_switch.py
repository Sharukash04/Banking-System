import account_dao
import bank

from in_memory_account_repository import InMemoryAccountRepository


print("Current repository:",type(account_dao.repository).__name__)


account_dao.accounts.clear()
account_dao.customer_index.clear()


account_dao.set_repository(
    InMemoryAccountRepository()
)


print(
    "Switched repository:",
    type(account_dao.repository).__name__
)


result=bank.create_account(
    301,
    "Repository Test",
    20,
    "9876543213",
    "Trichy",
    3000,
    "1234"
)


print("Account created:",result)


bank.deposit(301,1000)

print("Balance:",bank.get_balance(301))


print(
    "Account found:",
    account_dao.find_account(301).name
)


print(
    "JSON repository data remains separate:",
    account_dao.repository is not None
)