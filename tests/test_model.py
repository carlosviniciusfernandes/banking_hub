from unittest import TestCase
from unittest.mock import Mock, patch
from bank_controller import BankController

from user_interface.model import Model



class TestDataOutput(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.model = Model(service=Mock())

    def test_get_accounts_current_balance(self):
        self.model.banking_hub.list_balances.return_value = [
           '\ttest_account_1 - 100 BRL',
           '\ttest_account_2 - 1 BRL'
        ]
        expected_message = \
            'Account Balance:' + \
            '\n\ttest_account_1 - 100 BRL' + \
            '\n\ttest_account_2 - 1 BRL'

        message = self.model.get_accounts_current_balance()
        self.assertEqual(message, expected_message)
