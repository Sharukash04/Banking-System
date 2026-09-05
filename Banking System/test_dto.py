from account import Account
from account_dto import AccountDTO


account=Account(
    101,
    "Sharukash",
    19,
    "9876543210",
    "Trichy",
    5000,
    "1234"
)


dto=AccountDTO(
    account_id=account.account_id,
    name=account.name,
    age=account.age,
    phone=account.phone,
    address=account.address,
    balance=account.balance
)


print("DTO created successfully")
print("Account ID:",dto.account_id)
print("Name:",dto.name)
print("Balance:",dto.balance)

print("PIN exposed:",hasattr(dto,"pin"))
print("Transactions exposed:",hasattr(dto,"transactions"))