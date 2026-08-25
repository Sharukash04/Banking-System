from account import Account
from sorted_dict_service import add_account
from sorted_dict_service import get_accounts_by_id
from sorted_dict_service import get_accounts_by_balance
from sorted_dict_service import get_accounts_in_id_range
account1=Account(
    105,
    "Arun",
    20,
    "1111111111",
    "Trichy",
    3000,
    "1234"
)
account2=Account(
    101,
    "Sharukash",
    19,
    "2222222222",
    "Trichy",
    5000,
    "5678"
)
account3=Account(
    110,
    "Kumar",
    21,
    "3333333333",
    "Trichy",
    1000,
    "9999"
)
account4=Account(
    103,
    "Ravi",
    20,
    "4444444444",
    "Trichy",
    2000,
    "4567"
)
add_account(account1)
add_account(account2)
add_account(account3)
add_account(account4)
print("Accounts sorted by ID:")
for account in get_accounts_by_id():

    print(
        account.account_id,
        account.name,
        account.get_balance()
    )

print("\nAccounts sorted by Balance:")

for account in get_accounts_by_balance():
    print(
        account.account_id,
        account.name,
        account.get_balance()
    )
print("\nAccounts from ID 100 to 108:")
for account in get_accounts_in_id_range(100,108):
    print(
        account.account_id,
        account.name,
        account.get_balance()
    )