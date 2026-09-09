import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from account import Account
from transaction import Transaction


BASE_DIR=Path(__file__).resolve().parent

accounts_file=BASE_DIR/"accounts.json"
transactions_file=BASE_DIR/"transactions.json"


def json_serializer(value):

    if isinstance(value,datetime):
        return value.isoformat()

    raise TypeError("Type not supported")


def save_accounts(accounts):

    data=[]

    for account in accounts:

        account_data=asdict(account)

        account_data.pop("transactions",None)

        data.append(account_data)

    json_data=json.dumps(
        data,
        default=json_serializer,
        indent=4
    )

    accounts_file.write_text(json_data)


def save_transactions(accounts):

    data=[]
    saved_transactions=set()

    for account in accounts:

        for transaction in account.transactions:

            key=(
                transaction.transaction_type,
                transaction.amount,
                transaction.source_account,
                transaction.destination_account,
                transaction.timestamp.isoformat()
            )

            if key in saved_transactions:
                continue

            saved_transactions.add(key)

            data.append(asdict(transaction))

    json_data=json.dumps(
        data,
        default=json_serializer,
        indent=4
    )

    transactions_file.write_text(json_data)


def save_all(accounts):

    save_accounts(accounts)
    save_transactions(accounts)


def load_accounts():

    if not accounts_file.exists():
        return []

    json_data=accounts_file.read_text()

    data=json.loads(json_data)

    accounts=[]

    for item in data:

        account=Account(
            item["account_id"],
            item["name"],
            item["age"],
            item["phone"],
            item["address"],
            item["balance"],
            item["pin"],
            []
        )

        accounts.append(account)

    if not transactions_file.exists():
        return accounts

    transaction_data=json.loads(
        transactions_file.read_text()
    )

    account_lookup={}

    for account in accounts:
        account_lookup[account.account_id]=account

    for item in transaction_data:

        transaction=Transaction(
            item["transaction_type"],
            item["amount"],
            item["source_account"],
            item["destination_account"],
            datetime.fromisoformat(item["timestamp"])
        )

        source_account=account_lookup.get(
            transaction.source_account
        )

        destination_account=account_lookup.get(
            transaction.destination_account
        )

        if transaction.transaction_type=="TRANSFER":

            if source_account:
                source_account.transactions.append(transaction)

            if destination_account:
                destination_account.transactions.append(transaction)

        else:

            if source_account:
                source_account.transactions.append(transaction)

    return accounts
