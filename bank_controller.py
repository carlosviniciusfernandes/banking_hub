from banking_hub.bank_accounts.bank_account_model import BankAccount


class BankController:

    def __init__(self) -> None:
        self.bank_accounts: dict[str, BankAccount] = {}

    def add_bank_account(
        self,
        bank: str,
        account: BankAccount
    ) -> None:
        self.bank_accounts[bank] = account

    def remove_bank_account(self, bank: str) -> None:
        self.bank_accounts.pop(bank)

    def print_balances(self):
        pass

    def print_transaction(self):
        pass
