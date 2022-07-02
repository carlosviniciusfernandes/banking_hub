from datetime import datetime

from banking_hub_service import BankingHubService


class GUIModel:

    def __init__(self, banking_service: BankingHubService) -> None:
        self.banking_hub = banking_service

    def get_accounts_current_balance(self) -> str:
        message = 'Account Balance:'
        for balance in self.banking_hub.list_balances():
            message += f'\n\t{balance}'

        return message

    def get_accounts_transactions_in_timedelta(
        self,
        from_date: datetime,
        to_date: datetime = datetime.now()
    ) -> str:
        message = f'Transactions from {from_date} to {to_date}'

        transactions_dict = self.banking_hub.list_transactions(from_date, to_date)

        for account_name, transactions in transactions_dict.items():
            message += f'\n\t# {account_name}:'
            for index, transaction in enumerate(transactions):
                message += f'\n\t\t{index+1}. {transaction}'

        return message
