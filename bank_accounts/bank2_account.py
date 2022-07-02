from datetime import datetime
from typing import List, Tuple

from packages.bank2_integration import Bank2AccountSource

from .bank_account_model import BankAccount


class Bank2Account(BankAccount):

    def __init__(self, account_id: int) -> None:
        super().__init__()
        self.account_id = account_id

    def get_balance(self) -> Tuple[float, str]:
        raw_balance = Bank2AccountSource.get_balance(self.account_id)
        return raw_balance.balance, raw_balance.currency

    def get_transactions(
        self,
        from_date: datetime,
        to_date: datetime
    ) -> List[Tuple[float, int, str]]:
        self.validator_class.validate_transactions_timedelta(from_date, to_date)

        raw_transactions = Bank2AccountSource.get_transactions(
            account_id=self.account_id,
            from_date=from_date,
            to_date=to_date,
        )

        parsed_transactions = [
            (transaction.amount, transaction.type, transaction.text)
            for transaction in raw_transactions
        ]

        return parsed_transactions