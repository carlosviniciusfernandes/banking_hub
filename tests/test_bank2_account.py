from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import Mock, patch

from bank_accounts import Bank2Account
from packages.bank2_integration import Bank2AccountSource


class TestBank2Account(TestCase):

    @classmethod
    def setUpClass(self) -> None:
        super().setUpClass()
        self.bank_account: Bank2Account = Bank2Account(account_id=1234)

    @patch.object(Bank2AccountSource, 'get_balance')
    def test_get_account_balance(
        self,
        mock_get_balance: Mock,
    ):
        mock_get_balance.return_value = Mock(balance=100, currency='ETH')
        expected_balance = (100, 'ETH')

        balance = self.bank_account.get_balance()

        self.assertEqual(balance, expected_balance)
        mock_get_balance.assert_called_once_with(self.bank_account.account_id)

    @patch.object(Bank2AccountSource, 'get_transactions')
    def test_get_transactions(self, mock_get_transactions: Mock):
        today = datetime.now()
        yesterday = today - timedelta(days=1)

        mock_get_transactions.return_value = [
            Mock(amount=2, type=3, text='test transaction for bank2'),
            Mock(amount=20, type=4, text='another test transaction bank2'),
        ]

        expected_parsed_transactions = [
            (2, 3, 'test transaction for bank2'),
            (20, 4, 'another test transaction bank2')
        ]

        transactions = self.bank_account.get_transactions(
            from_date=today,
            to_date=yesterday
        )

        self.assertEqual(transactions, expected_parsed_transactions)
