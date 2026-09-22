from pydantic import BaseModel

class AccountCreate(BaseModel):

    account_id: int
    name: str
    age: int
    phone: str
    address: str
    balance: float
    pin: str

class AccountUpdate(BaseModel):

    name: str
    age: int
    phone: str
    address: str