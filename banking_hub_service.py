from datetime import datetime
from typing import Dict, List

from bank_accounts import BankAccount
from resources.errors import BankAccountNotFound, InvalidBankAccount


class BankingHubService:

    def __init__(self) -> None:
        self.bank_accounts: dict[str, BankAccount] = {}

    def add_bank_account(
        self,
        account_name: str,
        account: BankAccount,
    ) -> None:
        if isinstance(account, BankAccount):
            self.bank_accounts[account_name] = account
        else:
            raise InvalidBankAccount(
                f'Could not register the {account_name} account, please provide an account ' +
                'object that is a BankAccount sub-type'
            )

    def remove_bank_account(self, account_name: str) -> None:
        try:
            self.bank_accounts.pop(account_name)
        except KeyError:
            raise BankAccountNotFound(
                f'Could not find {account_name}, please check the registered banks accounts and try again'
            )

    def list_balances(self) -> List[str]:
        aggregated_balances = []
        for account_name, account in self.bank_accounts.items():
            amount, currency = account.get_balance()
            aggregated_balances.append(f'{account_name} - {amount} {currency}')
        return aggregated_balances

    def list_transactions(
        self,
        from_date: datetime,
        to_date: datetime = datetime.now()
    ) -> Dict[str, List[str]]:
        aggregated_transactions = {}
        for account_name, account in self.bank_accounts.items():
            aggregated_transactions[account_name] = []
            transactions = account.get_transactions(from_date, to_date)
            for transaction in transactions:
                value, currency, text = transaction
                aggregated_transactions[account_name].append(
                    f'{value} {currency} ({text})'
                )

        return aggregated_transactions
