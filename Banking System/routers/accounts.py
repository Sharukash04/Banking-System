from fastapi import APIRouter,Depends

from account_dto import AccountDTO
from services.account_service import AccountService
from dependencies import get_account_service


router=APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)


@router.get("/",response_model=list[AccountDTO])
def get_accounts(
    service:AccountService=Depends(get_account_service)
):

    return service.get_all_accounts()