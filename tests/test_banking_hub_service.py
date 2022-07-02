from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import Mock

from bank_accounts import BankAccount
from banking_hub_service import BankingHubService
from resources.errors import BankAccountNotFound, InvalidBankAccount


class TestBankingHubServiceSetup(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.controller = BankingHubService()

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
        controller = BankingHubService()

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


class TestBankingHubServiceDataAggregation(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.bank_controller = BankingHubService()

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
           'test_account_1 - 100 BRL',
           'test_account_2 - 1 BRL'
        ]

        balances = self.bank_controller.list_balances()
        self.assertEqual(balances, expected_balances)

    def test_list_transactions(self):
        to_date = datetime.now()
        from_date = to_date - timedelta(days=1)
        expected_transactions = {
          'test_account_1': [
                '70 BRL (Expensive Milk)',
                '10 BRL (Coke)'
            ],
            'test_account_2': [
                '250 BRL (Electricity bill)'
            ]
        }

        transactions = self.bank_controller.list_transactions(from_date, to_date)
        self.assertEqual(transactions, expected_transactions)
