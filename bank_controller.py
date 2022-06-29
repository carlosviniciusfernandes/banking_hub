from banking_hub.bank_accounts.bank_account_model import BankAccount
from banking_hub.resources.errors import (BankAccountNotFound,
                                          InvalidBankAccount)


class BankController:

    def __init__(self) -> None:
        self.bank_accounts: dict[str, BankAccount] = {}

    def add_bank_account(
        self,
        bank: str,
        account: BankAccount
    ) -> None:
        if isinstance(account, BankAccount):
            self.bank_accounts[bank] = account
        else:
            raise InvalidBankAccount(
                'Could not register account, please provide an account object that is a BankAccount sub-type'
            )

    def remove_bank_account(self, bank: str) -> None:
        try:
            self.bank_accounts.pop(bank)
        except KeyError:
            raise BankAccountNotFound(
                f'Could not find and account for {bank}, please check the registered banks account'
            )

    def print_balances(self):
        pass

    def print_transaction(self):
        pass
