from fastapi import Depends

from account_repository import AccountRepository
from json_account_repository import JsonAccountRepository
from services.account_service import AccountService


def get_repository()->AccountRepository:

    return JsonAccountRepository()


def get_account_service(
    repository:AccountRepository=Depends(get_repository)
)->AccountService:

    return AccountService(repository)
