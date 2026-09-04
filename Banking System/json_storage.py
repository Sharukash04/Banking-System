import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path


accounts_file=Path("accounts.json")
transactions_file=Path("transactions.json")


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

    return json.loads(json_data)