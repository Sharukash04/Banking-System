class Account:

    def __init__(self, account_id, name, age,
                 phone, address, balance, pin):
        self.account_id=account_id
        self.name=name
        self.age=age
        self.phone=phone
        self.address=address
        self.__balance=balance
        self.__pin=pin

    def deposit(self, amount):
        self.__balance+=amount

    def withdraw(self, amount):
        if amount<=self.__balance:
            self.__balance-=amount
            return True
        return False