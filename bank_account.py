from abc import ABC, abstractmethod


class BankAccount(ABC):

    @abstractmethod
    def get_balance():
        pass

    @abstractmethod
    def get_transactions():
        pass


class Bank1Account(BankAccount):
    pass


class Bank2Account(BankAccount):
    pass