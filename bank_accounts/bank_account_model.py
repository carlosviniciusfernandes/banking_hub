from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Tuple


class BankAccount(ABC):

    @abstractmethod
    def get_balance() -> Tuple[float, str]:
        pass

    @abstractmethod
    def get_transactions(
        from_date: datetime,
        to_date: datetime
    ) -> List[Tuple[float, int, str]]:
        pass
