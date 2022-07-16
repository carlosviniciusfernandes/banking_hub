from datetime import datetime, timedelta

from user_interface.gui_model import GUIModel


class GUIController:

    def __init__(self, model: GUIModel, view):
        self.model = model
        self.view = view

    def start(self):
        self.view.setup(self)
        self.view.start_main_loop()

    def handle_click_print_balances(self):
        data = self.model.get_accounts_current_balance()
        self.view.append_data_to_view(data)

    def handle_click_print_transactions(self):
        last_year = datetime.now() - timedelta(days=365)
        data = self.model.get_accounts_transactions_in_timedelta(from_date=last_year)
        self.view.append_data_to_view(data)

    def handle_click_clear_view(self):
        self.view.clear_data_from_view()