from banking_hub.bank_accounts.bank_account_model import BankAccount


class BankController:

    def __init__(self) -> None:
        self.bank_accounts: dict[str, BankAccount] = {}

    def add_bank_account(self):
        pass

    def remove_bank_account(self):
        pass

    def print_balances(self):
        pass

    def print_transaction(self):
        pass
