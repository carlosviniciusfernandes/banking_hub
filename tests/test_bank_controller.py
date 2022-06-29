from unittest import TestCase
from unittest.mock import Mock

from banking_hub.bank_accounts.bank_account_model import BankAccount
from banking_hub.bank_controller import BankController
from banking_hub.resources.errors import (BankAccountNotFound,
                                          InvalidBankAccount)


class TestBankControllerSetup(TestCase):

    def test_initialization(self):
        controller = BankController()
        self.assertEqual(controller.bank_accounts, {})

    def test_add_bank_account(self):
        mock_bank_account = Mock(spec=BankAccount)
        controller = BankController()

        controller.add_bank_account(
            bank='test_bank_account',
            account=mock_bank_account
        )

        self.assertEqual(controller.bank_accounts, {'test_bank_account':mock_bank_account})

    def test_add_invalid_bank_account_raise_error(self):
        mock_bank_account = Mock()
        controller = BankController()

        with self.assertRaises(InvalidBankAccount):
            controller.add_bank_account(
                bank='test_invalid_bank_account',
                account=mock_bank_account
            )
        self.assertEqual(controller.bank_accounts, {})

    def test_remove_bank_account(self):
        mock_bank_account = Mock(spec=BankAccount)
        controller = BankController()
        controller.bank_accounts['test_bank_account'] = mock_bank_account

        controller.remove_bank_account(
            bank='test_bank_account'
        )

        self.assertEqual(controller.bank_accounts, {})

    def test_fail_to_remove_bank_account_raises_error(self):
        mock_bank_account = Mock(spec=BankAccount)
        controller = BankController()
        controller.bank_accounts['test_bank_account'] = mock_bank_account

        with self.assertRaises(BankAccountNotFound):
            controller.remove_bank_account(
                bank='test_invalid_bank_account'
            )
        self.assertEqual(controller.bank_accounts, {'test_bank_account': mock_bank_account})


class TestBankControllerDataOutput(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.bank_controller = BankController()
        super().setUpClass()

    def test_print_balance(self):
        pass

    def test_print_transactions(self):
        pass
