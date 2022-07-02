from bank_accounts import Bank1Account, Bank2Account
from banking_hub_service import BankingHubService
from user_interface.gui_controller import GUIController
from user_interface.gui_model import GUIModel
from user_interface.views.tk_view import TkView

bank1_account_id = 1234
bank2_account_id = 123456

banking_hub = BankingHubService()
banking_hub.add_bank_account(
    account_name='bank1_SP',
    account=Bank1Account(bank1_account_id)
)
banking_hub.add_bank_account(
    account_name='bank2_RJ',
    account=Bank2Account(bank2_account_id)
)

gui_model = GUIModel(banking_service=banking_hub)

gui_controller = GUIController(model=gui_model, view=TkView())

if __name__ == "__main__":
    gui_controller.start()
