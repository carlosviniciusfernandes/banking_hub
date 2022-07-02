from ast import List
from datetime import datetime

from bank_controller import BankController


class Model:

    def __init__(self, service: BankController) -> None:
        self.banking_hub = service

    def get_accounts_current_balance(self) -> str:
        message = 'Account Balance:'
        for balance in self.banking_hub.list_balances():
            message += f'\n{balance}'

        return message

    def get_accounts_transactions_in_timedelta(
        self,
        from_date: datetime,
        to_date: datetime = datetime.now()
    ) -> str:
        pass
        # message = f'Transactions from {from_date} to {to_date}'

        # for account_name, account in self.banking_hub.bank_accounts.items():
        #     transactions = account.get_transactions(from_date, to_date)
        #     message += f'\n\t# {account_name}:'
        #     for index, transaction in enumerate(transactions):
        #         value, currency, text = transaction
        #         message += f'\n\t\t{index+1}. {value} {currency} ({text})'

        # return message
