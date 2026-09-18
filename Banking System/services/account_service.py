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


    def delete_account(self,account_id:int):

        return self.repository.delete(account_id)

