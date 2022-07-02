from datetime import datetime, timedelta
from unittest import TestCase

from bank_accounts.bank_account_model import OperationsValidator
from resources.errors import InvalidTimeInterval


class TestBankAccountOperationsValidators(TestCase):

    def test_valid_transactions_timedelta(self):
        from_date = datetime.now()
        to_date = from_date + timedelta(days=90)

        try:
            OperationsValidator.validate_transactions_timedelta(from_date, to_date)
        except Exception:
            self.fail()

    def test_invalid_trasactions_timedelta(self):
        from_date = datetime.now()

        with self.assertRaises(InvalidTimeInterval):
            to_date = from_date - timedelta(days=90)
            OperationsValidator.validate_transactions_timedelta(from_date, to_date)

        with self.assertRaises(InvalidTimeInterval):
            to_date = from_date + timedelta(days=400)
            OperationsValidator.validate_transactions_timedelta(from_date, to_date)
