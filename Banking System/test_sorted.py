from sorted_service import add_account
from sorted_service import get_account_ids
from sorted_service import get_ids_in_range
add_account(105)
add_account(101)
add_account(110)
add_account(103)
print("All account IDs:")
print(get_account_ids())
print("IDs from 100 to 108:")
print(get_ids_in_range(100,108))