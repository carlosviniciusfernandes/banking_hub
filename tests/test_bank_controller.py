from unittest import TestCase
from unittest.mock import Mock

from banking_hub.bank_accounts.bank_account_model import BankAccount
from banking_hub.bank_controller import BankController


class TestBankControllerSetup(TestCase):

    def test_initialization(self):
        controller = BankController()
        self.assertEqual(controller.bank_accounts, {})

    def test_add_bank_account(self):
        mock_bank_account = Mock(spec=BankAccount)
        controller = BankController()

        controller.add_bank_account(
            bank='test_bank_account',
            acccount=mock_bank_account
        )

        self.assertEqual(controller.bank_accounts, {'test_bank_account':mock_bank_account})

    def test_remove_bank_account(self):
        mock_bank_account = Mock(spec=BankAccount)
        controller = BankController()
        controller.bank_accounts['test_bank_account'] = mock_bank_account

        controller.add_remove_account(
            bank='test_bank_account'
        )

        self.assertEqual(controller.bank_accounts, {})


class TestBankControllerDataOutput(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.bank_controller = BankController()
        super().setUpClass()

    def test_print_balance():
        pass

    def test_print_transactions():
        pass
