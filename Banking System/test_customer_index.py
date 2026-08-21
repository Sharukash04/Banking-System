from bank import create_account
from account_dao import find_accounts_by_name


create_account(
    101,
    "Sharukash",
    19,
    "1234567890",
    "Trichy",
    1000,
    "1234"
)

create_account(
    102,
    "Arun",
    20,
    "9876543210",
    "Trichy",
    2000,
    "5678"
)

create_account(
    103,
    "Sharukash",
    19,
    "1111111111",
    "Trichy",
    3000,
    "9999"
)


accounts=find_accounts_by_name("Sharukash")

print("Accounts with name Sharukash:")

for account in accounts:
    print(
        account.account_id,
        account.name,
        account.get_balance()
    )