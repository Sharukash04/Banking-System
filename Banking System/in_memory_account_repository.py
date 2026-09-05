from typing import Optional

from account import Account
from account_repository import AccountRepository


class InMemoryAccountRepository(AccountRepository):

    def __init__(self):

        self.accounts={}


    def save(self,account:Account)->None:

        self.accounts[account.account_id]=account


    def get(self,account_id:int)->Optional[Account]:

        return self.accounts.get(account_id)


    def list(self)->list[Account]:

        return list(self.accounts.values())


    def delete(self,account_id:int)->bool:

        if account_id in self.accounts:

            del self.accounts[account_id]

            return True

        return False