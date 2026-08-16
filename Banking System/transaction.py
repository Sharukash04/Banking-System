from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:

    transaction_type: str
    amount: float
    source_account: int
    destination_account: int
    timestamp: datetime