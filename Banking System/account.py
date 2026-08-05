class Account:
    def __init__(self,acc_id,name,age,phone,address,balance,pin):
        self.acc_id=acc_id
        self.name=name
        self.age=age
        self.phone=phone
        self.address=address
        self.__balance=balance
        self.__pin=pin

    #Add money to account
    def deposit(self,amount):
        self.__balance+=amount

    #Remove money if sufficient balance
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            return True
        return False

    #Get current balance
    def get_balance(self):
        return self.__balance

    #Verify PIN for security
    def verify_pin(self,pin):
        return self.__pin==pin

    #Change PIN after verification
    def change_pin(self,old_pin,new_pin):
        if self.__pin==old_pin:
            self.__pin=new_pin
            return True
        return False