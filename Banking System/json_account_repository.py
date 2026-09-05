from typing import Optional

from account import Account
from account_repository import AccountRepository
from json_storage import save_accounts,load_accounts


class JsonAccountRepository(AccountRepository):

    def save(self,account:Account)->None:

        accounts=self.list()

        found=False

        for index,item in enumerate(accounts):

            if item.account_id==account.account_id:

                accounts[index]=account
                found=True
                break

        if not found:

            accounts.append(account)

        save_accounts(accounts)


    def get(self,account_id:int)->Optional[Account]:

        accounts=self.list()

        for account in accounts:

            if account.account_id==account_id:
                return account

        return None


    def list(self)->list[Account]:

        return load_accounts()


    def delete(self,account_id:int)->bool:

        accounts=self.list()

        for account in accounts:

            if account.account_id==account_id:

                accounts.remove(account)
                save_accounts(accounts)

                return True

        return False