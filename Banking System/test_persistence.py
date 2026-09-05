import account_dao
import bank


account_dao.accounts.clear()
account_dao.customer_index.clear()


account=bank.create_account(
    201,
    "Persistence Test",
    20,
    "9876543212",
    "Trichy",
    5000,
    "1234"
)

print("Account created:",account)


bank.deposit(201,1000)

print("Balance after deposit:",bank.get_balance(201))


bank.withdraw(201,500)

print("Balance after withdrawal:",bank.get_balance(201))