from account import Account
import account_dao


# Create new account with unique ID
def create_account(acc_id, name, age, phone, address, balance, pin):

    if account_dao.account_exists(acc_id):
        return False

    acc = Account(
        acc_id,
        name,
        age,
        phone,
        address,
        balance,
        pin
    )

    account_dao.add_account(acc)

    return True


# Find account
def find_account(acc_id):

    return account_dao.find_account(acc_id)


# Deposit money
def deposit(acc_id, amount):

    acc = account_dao.find_account(acc_id)

    if acc:
        acc.deposit(amount)
        return True

    return False


# Withdraw money
def withdraw(acc_id, amount):

    acc = account_dao.find_account(acc_id)

    if acc:
        return acc.withdraw(amount)

    return False


# Get account balance
def get_balance(acc_id):

    acc = account_dao.find_account(acc_id)

    if acc:
        return acc.get_balance()

    return None


# Display all accounts in insertion order
def display_accounts():

    accounts = account_dao.get_all_accounts()

    if not accounts:
        print("No accounts in bank")
        return

    print("\n========== BANK ACCOUNTS ==========")
    print("ID     Name           Balance")
    print("-----------------------------------")

    for acc in accounts:
        print(
            f"{acc.account_id:<6}"
            f"{acc.name:<15}"
            f"{acc.get_balance():.2f}"
        )

    print("===================================\n")


# Change account PIN
def change_pin(acc_id, old_pin, new_pin):

    acc = account_dao.find_account(acc_id)

    if acc:
        return acc.change_pin(old_pin, new_pin)

    return False


# Remove account
def close_account(acc_id, pin):

    acc = account_dao.find_account(acc_id)

    if acc and acc.verify_pin(pin):
        return account_dao.delete_account(acc_id)

    return False