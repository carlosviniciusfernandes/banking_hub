from datetime import datetime, timedelta
import pdb

from user_interface.model import Model

class GUIController:

    def __init__(self, model: Model, view):
        self.model = model
        self.view = view

    def start(self):
        self.view.setup(self)
        self.view.start_main_loop()

    def handle_click_print_balances(self):
        message = self.model.get_accounts_current_balance()
        self.view.append_data_to_view(message)

    def handle_click_print_transactions():
        pass
    #     last_year = datetime.now() - timedelta(days=365)
    #     message = self.model.get_accounts_transactions_in_timedelta(from_date=last_year)
    #     for item in message.split('\n'):
    #         self.view.append_to_list(self.view, item=item.replace('\t', '    '))

    def handle_click_clear_view(self):
        self.view.clear_data_from_view()