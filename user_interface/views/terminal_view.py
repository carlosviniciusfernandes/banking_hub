import os

from user_interface.gui_controller import GUIController
from user_interface.views import BaseView


class TerminalView(BaseView):

    def setup(self, controller: GUIController):
        self.command_map = {
            'print_balances': controller.handle_click_print_balances,
            'print_transactions': controller.handle_click_print_transactions,
            'clear': controller.handle_click_clear_view,
            'help': self.show_available_commands,
            'exit': self.force_quit,
        }

    def append_data_to_view(self, data: str):
        print(data)

    def clear_data_from_view(self):
        os.system('clear')

    def start_main_loop(self):
        print('-=- Welcome to Banking Hub -=- ')
        self.show_available_commands()

        user_input = None
        try:
            while user_input != 'exit':
                user_input = input('How may I help?\t')
                self.command_map[user_input]()
        except (KeyboardInterrupt, EOFError):
            print('\nbye!!!')

    def show_available_commands(self):
        print('Available commands:')
        for key, _ in self.command_map.items():
            print(f'# {key}')

    def force_quit(self):
        raise KeyboardInterrupt