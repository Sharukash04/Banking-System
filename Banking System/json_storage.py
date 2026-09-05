import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from account import Account
from transaction import Transaction


accounts_file=Path("accounts.json")


def json_serializer(value):

    if isinstance(value,datetime):
        return value.isoformat()

    raise TypeError("Type not supported")


def save_accounts(accounts):

    data=[]

    for account in accounts:

        data.append(asdict(account))

    json_data=json.dumps(
        data,
        default=json_serializer,
        indent=4
    )

    accounts_file.write_text(json_data)


def load_accounts():

    if not accounts_file.exists():
        return []

    json_data=accounts_file.read_text()

    data=json.loads(json_data)

    accounts=[]

    for item in data:

        transactions=[]

        for transaction_data in item["transactions"]:

            transaction=Transaction(
                transaction_data["transaction_type"],
                transaction_data["amount"],
                transaction_data["source_account"],
                transaction_data["destination_account"],
                datetime.fromisoformat(transaction_data["timestamp"])
            )

            transactions.append(transaction)

        account=Account(
            item["account_id"],
            item["name"],
            item["age"],
            item["phone"],
            item["address"],
            item["balance"],
            item["pin"],
            transactions
        )

        accounts.append(account)

    return accounts