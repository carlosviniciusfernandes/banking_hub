from banking_hub.bank_accounts.bank_account_model import BankAccount


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
            raise TypeError('Invalid Type, please provide an account that is a BankAccount sub-type')

    def remove_bank_account(self, bank: str) -> None:
        self.bank_accounts.pop(bank)

    def print_balances(self):
        pass

    def print_transaction(self):
        pass
