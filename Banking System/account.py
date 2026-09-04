from dataclasses import dataclass,field
@dataclass
class Account:
    account_id: int
    name: str
    age: int
    phone: str
    address: str
    balance: float
    pin: str
    transactions: list=field(default_factory=list)
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def verify_pin(self,pin):
        return self.pin==pin

    def change_pin(self,old_pin,new_pin):
        if self.pin==old_pin:
            self.pin=new_pin
            return True
        return False