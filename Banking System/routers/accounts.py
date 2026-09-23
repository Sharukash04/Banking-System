from fastapi import APIRouter,Depends,HTTPException

from account import Account
from account_dto import AccountDTO
from account_request import AccountCreate,AccountUpdate,TransferRequest
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


@router.get("/{account_id}",response_model=AccountDTO)
def get_account(
    account_id:int,
    service:AccountService=Depends(get_account_service)
):
    account=service.get_account(account_id)

    if account is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return account


@router.post("/",response_model=AccountDTO,status_code=201)
def create_account(
    account_data:AccountCreate,
    service:AccountService=Depends(get_account_service)
):
    account=Account(
        account_data.account_id,
        account_data.name,
        account_data.age,
        account_data.phone,
        account_data.address,
        account_data.balance,
        account_data.pin
    )

    created=service.create_account(account)

    if not created:
        raise HTTPException(
            status_code=409,
            detail="Account already exists"
        )

    return account


@router.put("/{account_id}",response_model=AccountDTO)
def update_account(
    account_id:int,
    account_data:AccountUpdate,
    service:AccountService=Depends(get_account_service)
):
    account=service.update_account(account_id,account_data)

    if account is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return account


@router.delete("/{account_id}")
def delete_account(
    account_id:int,
    service:AccountService=Depends(get_account_service)
):
    deleted=service.delete_account(account_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return {
        "message":"Account deleted successfully"
    }


@router.post("/transfer")
def transfer(
    transfer_data:TransferRequest,
    service:AccountService=Depends(get_account_service)
):
    transferred=service.transfer(
        transfer_data.from_id,
        transfer_data.to_id,
        transfer_data.amount
    )

    if not transferred:
        raise HTTPException(
            status_code=400,
            detail="Transfer failed"
        )

    return {
        "message":"Transfer successful"
    }
