from account import Account
from account_repository import AccountRepository


class AccountService:

    def __init__(self,repository:AccountRepository):

        self.repository=repository


    def get_all_accounts(self):

        return self.repository.list()


    def get_account(self,account_id:int):

        return self.repository.get(account_id)


    def create_account(self,account:Account):

        existing_account=self.repository.get(account.account_id)

        if existing_account is not None:

            return False

        self.repository.save(account)

        return True


    def update_account(self,account_id:int,account_data):

        account=self.repository.get(account_id)

        if account is None:

            return None

        account.name=account_data.name
        account.age=account_data.age
        account.phone=account_data.phone
        account.address=account_data.address

        self.repository.save(account)

        return account


    def transfer(self,from_id,to_id,amount):

        sender=self.repository.get(from_id)
        receiver=self.repository.get(to_id)

        if sender is None or receiver is None:
            return False

        if amount<=0:
            return False

        if not sender.withdraw(amount):
            return False

        receiver.deposit(amount)

        self.repository.save(sender)
        self.repository.save(receiver)

        return True


    def delete_account(self,account_id:int):

        return self.repository.delete(account_id)
