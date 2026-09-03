from account import Account


account=Account(
    101,
    "Sharukash",
    19,
    "9876543210",
    "Trichy",
    5000,
    "1234"
)


print("Account:",account.name)
print("Balance:",account.get_balance())

account.deposit(1000)

print("After deposit:",account.get_balance())

account.withdraw(500)

print("After withdrawal:",account.get_balance())

print("PIN correct:",account.verify_pin("1234"))