from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import Mock, patch

from bank_accounts import BankAccount
from bank_controller import BankController
from resources.errors import BankAccountNotFound, InvalidBankAccount


class TestBankControllerSetup(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.controller = BankController()

    def test_initialization(self):
        self.assertEqual(self.controller.bank_accounts, {})

    def test_add_bank_account(self):
        mock_bank_account = Mock(spec=BankAccount)

        self.controller.add_bank_account(
            account_name='test_bank_account',
            account=mock_bank_account
        )

        self.assertEqual(self.controller.bank_accounts, {'test_bank_account':mock_bank_account})

    def test_add_invalid_bank_account_raise_error(self):
        mock_bank_account = Mock()
        controller = BankController()

        with self.assertRaises(InvalidBankAccount):
            controller.add_bank_account(
                account_name='test_invalid_bank_account',
                account=mock_bank_account
            )
        self.assertEqual(controller.bank_accounts, {})

    def test_remove_bank_account(self):
        mock_bank_account = Mock(spec=BankAccount)
        self.controller.bank_accounts['test_bank_account'] = mock_bank_account

        self.controller.remove_bank_account(
            account_name='test_bank_account'
        )

        self.assertEqual(self.controller.bank_accounts, {})

    def test_fail_to_remove_bank_account_raises_error(self):
        mock_bank_account = Mock(spec=BankAccount)
        self.controller.bank_accounts['test_bank_account'] = mock_bank_account

        with self.assertRaises(BankAccountNotFound):
            self.controller.remove_bank_account(
                account_name='test_invalid_bank_account'
            )
        self.assertEqual(self.controller.bank_accounts, {'test_bank_account': mock_bank_account})


class TestBankControllerDataAggregation(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.bank_controller = BankController()

        account_1 = Mock(spec=BankAccount)
        account_1.get_balance.return_value = (100, 'BRL')
        account_1.get_transactions.return_value = [(70, 'BRL', 'Expensive Milk'), (10, 'BRL', 'Coke')]

        account_2 = Mock(spec=BankAccount)
        account_2.get_balance.return_value = (1, 'BRL')
        account_2.get_transactions.return_value = [(250, 'BRL', 'Electricity bill')]

        cls.bank_controller.add_bank_account(account_name='test_account_1', account=account_1)
        cls.bank_controller.add_bank_account(account_name='test_account_2', account=account_2)

    def test_list_balances(self):
        expected_balances = [
           '\ttest_account_1 - 100 BRL',
           '\ttest_account_2 - 1 BRL'
        ]

        balances = self.bank_controller.list_balances()
        self.assertEqual(balances, expected_balances)

    @patch('builtins.print')
    def test_print_transactions(self, mock_print: Mock):
        to_date = datetime.now()
        from_date = to_date - timedelta(days=1)
        expected_message = \
            f'Transactions from {from_date} to {to_date}' + \
            '\n\t# test_account_1:' + \
            '\n\t\t1. 70 BRL (Expensive Milk)' + \
            '\n\t\t2. 10 BRL (Coke)' + \
            '\n\t# test_account_2:' + \
            '\n\t\t1. 250 BRL (Electricity bill)'

        self.bank_controller.print_transaction(from_date, to_date)

        mock_print.assert_called_once_with(expected_message)
