from user_interface.gui_controller import GUIController
from user_interface.views.base_view import View


class TerminalView(View):

    def setup(self, controller: GUIController):
        """ TDB - map controller inputs to keywords command in terminal """
        pass

    def append_data_to_view(self, data: str):
        print(data)

    def clear_data_from_view(self):
        """ To be implemented - idea is to clear the terminal window """
        pass

    def start_main_loop(self):
        """ To be implemented - idea is to have a loop that waits user input """
        pass
