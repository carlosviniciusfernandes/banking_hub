from datetime import datetime, timedelta

from bank_accounts import BankAccount
from resources.errors import BankAccountNotFound, InvalidBankAccount
from views.base_view import View


class BankController:

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

    def print_balances(self) -> None:
        message = 'Account Balance:'
        for account_name, account in self.bank_accounts.items():
            amount, currency = account.get_balance()
            message += f'\n{account_name} - {amount} {currency}'

        # print(message)
        return message

    def print_transaction(
        self,
        from_date: datetime,
        to_date: datetime = datetime.now()
    ) -> None:
        message = f'Transactions from {from_date} to {to_date}'

        for account_name, account in self.bank_accounts.items():
            transactions = account.get_transactions(from_date, to_date)
            message += f'\n\t# {account_name}:'
            for index, transaction in enumerate(transactions):
                value, currency, text = transaction
                message += f'\n\t\t{index+1}. {value} {currency} ({text})'

        # print(message)
        return message

class Controller:

    def __init__(self, controller, view: View):
        self.controller = controller
        self.view = view

    def start(self):
        self.view.setup(self.view, self)
        self.view.start_main_loop(self.view)

    def handle_click_print_balances(self):
        message = self.controller.print_balances()
        for item in message.split('\n'):
            self.view.append_to_list(self.view, item=item)

    def handle_click_print_transaction(self):
        last_year = datetime.now() - timedelta(days=365)
        message = self.controller.print_transaction(from_date=last_year)
        for item in message.split('\n'):
            self.view.append_to_list(self.view, item=item.replace('\t', '    '))

    def handle_click_clear_list(self):
        self.view.clear_list(self.view)