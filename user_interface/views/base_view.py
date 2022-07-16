from abc import ABC, abstractmethod

from user_interface.gui_controller import GUIController


class BaseView(ABC):
    @abstractmethod
    def setup(self, controller: GUIController):
        pass

    @abstractmethod
    def append_data_to_view(self, data):
        pass

    @abstractmethod
    def clear_data_from_view(self):
        pass

    @abstractmethod
    def start_main_loop(self):
        pass