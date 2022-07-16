from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import Mock

from user_interface.gui_model import GUIModel


class TestMessageModelDataOutput(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.model = GUIModel(banking_service=Mock())

    def test_get_accounts_current_balance(self):
        self.model.banking_hub.list_balances.return_value = [
           'test_account_1 - 100 BRL',
           'test_account_2 - 1 BRL'
        ]
        expected_message = \
            'Account Balance:' + \
            '\n\ttest_account_1 - 100 BRL' + \
            '\n\ttest_account_2 - 1 BRL'

        message = self.model.get_accounts_current_balance()
        self.assertEqual(message, expected_message)

    def test_get_accounts_transactions_in_timedelta(self):
        to_date = datetime.now()
        from_date = to_date - timedelta(days=1)
        self.model.banking_hub.list_transactions.return_value = {
            'test_account_1': [
                '70 BRL (Expensive Milk)',
                '10 BRL (Coke)'
            ],
            'test_account_2': [
                '250 BRL (Electricity bill)'
            ]
        }
        expected_message = \
            f'Transactions from {from_date} to {to_date}' + \
            '\n\t# test_account_1:' + \
            '\n\t\t1. 70 BRL (Expensive Milk)' + \
            '\n\t\t2. 10 BRL (Coke)' + \
            '\n\t# test_account_2:' + \
            '\n\t\t1. 250 BRL (Electricity bill)'

        message = self.model.get_accounts_transactions_in_timedelta(from_date, to_date)
        self.assertEqual(message, expected_message)
