from bank_accounts import Bank1Account, Bank2Account
from bank_controller import BankController, Controller
from views.tk_view import TkView

bank1_account_id = 1234
bank2_account_id = 123456

bank_controller = BankController()
controller = Controller(bank_controller, TkView)

bank_controller.add_bank_account(
    account_name='bank1_SP',
    account=Bank1Account(bank1_account_id)
)
bank_controller.add_bank_account(
    account_name='bank2_RJ',
    account=Bank2Account(bank2_account_id)
)

if __name__ == "__main__":
    # controller.print_balances()

    # from datetime import datetime
    # from_date = datetime.now()
    # controller.print_transaction(from_date)
    controller.start()
