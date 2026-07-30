def login():
    print("WELCOME TO LOGIN PAGE")
    print("If you are already registered please enter your credentials")
    while True:
        username=input("Enter your username:")
        password=input("Enter your password:")
        for i in users:
            if i.username==username and i.password==password:
                print("Login successful")
                return