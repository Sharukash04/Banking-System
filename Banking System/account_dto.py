from pydantic import BaseModel


class AccountDTO(BaseModel):

    account_id: int
    name: str
    age: int
    phone: str
    address: str
    balance: float