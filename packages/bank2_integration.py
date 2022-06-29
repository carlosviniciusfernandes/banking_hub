from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto


@dataclass(frozen=True)
class Bank2AccountBalance:
    balance: float
    currency: str


class TransactionTypes(Enum):
    CREDIT = auto()
    DEBIT= auto()


@dataclass(frozen=True)
class Bank2Transaction:

    amount: float
    type: int
    text: str

    def validate_type(self):
        if self.type not in [enum.value for enum in TransactionTypes]:
            raise Exception("Not a valid operation type!")

    def __post_init__(self):
        self.validate_type()


class Bank2AccountSource:

    def get_balance(account_num: int) -> Bank2AccountBalance:
        return Bank2AccountBalance(512.5, "USD")

    def get_transactions(account_id: int, from_date: datetime, to_date: datetime) -> list:
        return [
            Bank2Transaction(125, TransactionTypes.DEBIT.value, "Amazon.com"),
            Bank2Transaction(500, TransactionTypes.DEBIT.value, "Car insurance"),
            Bank2Transaction(800, TransactionTypes.CREDIT.value, "Salary")
        ]
