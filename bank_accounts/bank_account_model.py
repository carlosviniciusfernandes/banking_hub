from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import List, Tuple

from resources.errors import InvalidTimeInterval


class BankAccount(ABC):

    def __init__(self) -> None:
        self.validator_class = OperationsValidator

    @abstractmethod
    def get_balance() -> Tuple[float, str]:
        pass

    @abstractmethod
    def get_transactions(
        from_date: datetime,
        to_date: datetime
    ) -> List[Tuple[float, int, str]]:
        pass


class OperationsValidator:

    @staticmethod
    def validate_transactions_timedelta(
        from_date: datetime,
        to_date: datetime
    ) -> None:
        max_timedelta = timedelta(days=365)
        if from_date >= to_date or to_date - from_date > max_timedelta:
            raise InvalidTimeInterval(
                f'Please provide a valid time interval, to_date must be a date past of from_date' +
                'and the maximum time interval supported is 365 days.'
            )
