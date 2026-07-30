print("="*15 + " Quickbasket " + "="*15)
print()
print()
print("\tWELCOME TO QUICKBASKET")
print("Fresh essentials delivered in just 30 minutes")

content='''
1. Login
2. Register
3. Browse Categories
4. Search Product
5. View Cart
6. Checkout
7. My Orders
8. My Profile
9. Logout
10. Exit'''
print(content)
while True:
    choice=int(input("Enter the number regarding to your choice:"))

    if choice == 1:
        from login import login
        login()

    elif choice == 2:
        from Register import register
        register()