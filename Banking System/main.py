from fastapi import FastAPI,Depends,HTTPException

from account_dto import AccountDTO
from json_account_repository import JsonAccountRepository


app=FastAPI()


def get_repository():

    return JsonAccountRepository()


@app.get("/accounts",response_model=list[AccountDTO])
def get_accounts(repository:JsonAccountRepository=Depends(get_repository)):

    accounts=repository.list()

    return accounts


@app.get("/accounts/{account_id}",response_model=AccountDTO)
def get_account(account_id:int,repository:JsonAccountRepository=Depends(get_repository)):

    account=repository.get(account_id)

    if account is None:

        raise HTTPException(status_code=404,detail="Account not found")

    return account