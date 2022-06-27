from dataclasses import dataclass
from datetime import datetime


class Bank1AccountSource:

    def get_account_balance(account_id: int) -> float:
        return 215.5

    def get_account_currency(account_id: int) -> str:
        return "USD"

    def get_transactions(account_id: int, from_date: datetime, to_date: datetime) -> list:
        return [
            Bank1Transaction(100, Bank1Transaction.TYPE_CREDIT, "Check deposit"),
            Bank1Transaction(25.5, Bank1Transaction.TYPE_DEBIT, "Debit card purchase"),
            Bank1Transaction(225, Bank1Transaction.TYPE_DEBIT, "Rent payment")
        ]


@dataclass(frozen=True)
class Bank1Transaction:
    TYPE_CREDIT = 1
    TYPE_DEBIT = 2

    amount: float
    type: int
    text: str

    def validate_type(self):
        if self.type not in [self.TYPE_CREDIT, self.TYPE_DEBIT]:
            raise Exception("Not a valid operation type!")

    def __post_init__(self):
        self.validate_type()
