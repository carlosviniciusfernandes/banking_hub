import tkinter as tk

from views.base_view import View


class TkView(View):
    """ Based on Arjan's TK View example in his MVC lecture.

        ref: https://github.com/ArjanCodes/betterpython/blob/cb616a049ec4e4d6a7541ed41cc41238563dea9c/8%20-%20mvc/mvc-after.py#L1
    """

    def setup(self, controller):

        # setup tkinter
        self.root = tk.Tk()
        self.root.geometry("640x480")
        self.root.title("Banking Hub")

        # create the gui
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)

        self.list = tk.Listbox(self.frame)
        self.list.pack(fill=tk.BOTH, expand=1)

        self.get_balance_button = tk.Button(
            self.frame,
            text="Get Balances",
            command=controller.handle_click_print_balances
        )
        self.get_balance_button.pack()

        self.get_transactions_button = tk.Button(
            self.frame,
            text="Get Transactions",
            command=controller.handle_click_print_transaction
        )
        self.get_transactions_button.pack()

        self.clear_button = tk.Button(
            self.frame,
            text="Clear",
            command=controller.handle_click_clear_list
        )
        self.clear_button.pack()

    def append_to_list(self, item):
        self.list.insert(tk.END, item)

    def clear_list(self):
        self.list.delete(0, tk.END)

    def start_main_loop(self):
        # start the loop
        self.root.mainloop()
