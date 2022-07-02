from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def setup(self, controller):
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