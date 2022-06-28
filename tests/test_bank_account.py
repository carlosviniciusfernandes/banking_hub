from unittest import TestCase
from unittest.mock import Mock, patch


from banking_hub.bank_account import Bank1Account, BankAccount
from banking_hub.packages.bank1 import Bank1AccountSource


class TestBank1Account(TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.bank_account: Bank1Account = Bank1Account(account_id=1234)
        super().setUpClass()

    @patch.object(Bank1AccountSource, 'get_account_currency')
    @patch.object(Bank1AccountSource, 'get_account_balance')
    def test_get_account_balance(
        self,
        mock_get_balance: Mock,
        mock_get_currency: Mock
    ):
        mock_get_balance.return_value = 100
        mock_get_currency.return_value = "BTC"
        expected_balance = (100, "BTC")

        balance = self.bank_account.get_balance()

        self.assertEqual(balance, expected_balance)
        mock_get_balance.assert_called_once_with(self.bank_account.account_id)
        mock_get_currency.assert_called_once_with(self.bank_account.account_id)

    def test_get_transactions(self):
        pass