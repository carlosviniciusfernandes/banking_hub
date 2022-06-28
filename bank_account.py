from abc import ABC, abstractmethod
from datetime import datetime
from typing import Tuple

from banking_hub.packages.bank1 import Bank1AccountSource


class BankAccount(ABC):

    @abstractmethod
    def get_balance():
        pass

    @abstractmethod
    def get_transactions():
        pass


class Bank1Account(BankAccount):

    def __init__(self, account_id) -> None:
        self.account_id:int = account_id

    def get_balance(self) -> Tuple[float, str]:
        amount = Bank1AccountSource.get_account_balance(self.account_id)
        currency = Bank1AccountSource.get_account_currency(self.account_id)
        return amount, currency

    def get_transactions(
        self,
        from_date: datetime,
        to_date: datetime
    ) -> Tuple[float, int, str]:
        raw_transactions = Bank1AccountSource.get_transactions(
            account_id=self.account_id,
            from_date=from_date,
            to_date=to_date,
        )

        parsed_transactions = [
            (transaction.amount, transaction.type, transaction.text)
            for transaction in raw_transactions
        ]

        return parsed_transactions

class Bank2Account(BankAccount):
    pass