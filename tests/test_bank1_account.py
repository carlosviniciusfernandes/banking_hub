from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import Mock, patch

from bank_accounts import Bank1Account
from packages.bank1_integration import Bank1AccountSource


class TestBank1Account(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.bank_account: Bank1Account = Bank1Account(account_id=1234)

    @patch.object(Bank1AccountSource, 'get_account_currency')
    @patch.object(Bank1AccountSource, 'get_account_balance')
    def test_get_account_balance(
        self,
        mock_get_balance: Mock,
        mock_get_currency: Mock
    ):
        mock_get_balance.return_value = 100
        mock_get_currency.return_value = 'BTC'
        expected_balance = (100, 'BTC')

        balance = self.bank_account.get_balance()

        self.assertEqual(balance, expected_balance)
        mock_get_balance.assert_called_once_with(self.bank_account.account_id)
        mock_get_currency.assert_called_once_with(self.bank_account.account_id)

    @patch.object(Bank1AccountSource, 'get_transactions')
    def test_get_transactions(self, mock_get_transactions: Mock):
        today = datetime.now()
        yesterday = today - timedelta(days=1)

        mock_get_transactions.return_value = [
            Mock(amount=1, type=1, text='test transaction'),
            Mock(amount=10, type=2, text='another test transaction'),
        ]

        expected_parsed_transactions = [
            (1, 1, 'test transaction'),
            (10, 2, 'another test transaction')
        ]

        transactions = self.bank_account.get_transactions(
            from_date=today,
            to_date=yesterday
        )

        self.assertEqual(transactions, expected_parsed_transactions)
