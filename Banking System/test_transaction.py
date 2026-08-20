from bank import create_account
from bank import deposit
from bank import withdraw
from bank import transfer
from bank import get_balance
from bank import reverse_last_transaction


print("========== TEST 1: DEPOSIT REVERSAL ==========")

create_account(1,"Test User",19,"1234567890","Trichy",1000,"1234")

print("Before deposit:",get_balance(1))

deposit(1,500)

print("After deposit:",get_balance(1))

reverse_last_transaction(1)

print("After reverse:",get_balance(1))


print("\n========== TEST 2: WITHDRAWAL REVERSAL ==========")

withdraw(1,200)

print("After withdrawal:",get_balance(1))

reverse_last_transaction(1)

print("After reverse:",get_balance(1))


print("\n========== TEST 3: TRANSFER REVERSAL ==========")

create_account(2,"Test User 2",19,"9876543210","Trichy",500,"5678")

print("Account 1 before transfer:",get_balance(1))
print("Account 2 before transfer:",get_balance(2))

transfer(1,2,300)

print("Account 1 after transfer:",get_balance(1))
print("Account 2 after transfer:",get_balance(2))

reverse_last_transaction(1)

print("Account 1 after reverse:",get_balance(1))
print("Account 2 after reverse:",get_balance(2))


print("\n========== TEST 4: NO TRANSACTION ==========")

result=reverse_last_transaction(1)

print("Reverse result:",result)