# banking_hub

This a simple bank aggregation python application for displaying info from different banks in a uniform format, working like a personal _banking hub_ for the user. The ideia is that each integrated bank may have a different response format when pulling information from it. The application translates and displays that info into a particular format.

Code wise, the application is very simple, it doesn't require any external python packages, or that you build a virtual env just for it. It is only necessary that your system has python 3.7 or newer verions of python.

---
###  External Packages / Dependencies

The packages modules represents API integration with two hypothetical banks (__bank1__ and __bank2__).
```
banking_hub/
+-- packages/
    +-- bank1_integration.py
    +-- bank2_integration.py
```
Since this packages represents external API wrappers, they will mocked dependencies while testing the application modules/classes.

---
### BankAccount classes
The `BankAccount` class is an abstract class that translates a protocol that the application works with. Every bank integration whitin the application must implement as `BankAccount` sub-class.
The `Bank1Account` and `Bank2Account` classes are the implementations of the `BankAccount` for their respective bank integrations (In a way, they are functional adapters for the bank integrations to the application protocol/format).

__Note__: I decided to keep the application simple as possible and compatible with older version of python 3 (3.7+). For python 3.8+, it is possible to use python `Protocol` to represent this abstraction layer instead of `abc.ABC` abstract base class.
```
banking_hub/
+-- bank_accounts/
    +-- __init__.py
    +-- bank_account_model.py
    +-- bank1_account.py
    +-- bank2_account.py
```

---
### Testing
For keeping the application simple, python's builtin `unittest` is used. The test are writter using `unittest.TesCase`.

For running test using `unittest` as the test runner:
> $ python3 -m unittest tests

__Note__: If want a `pytest` as the test runner, you can but you will need to install it yourself (which is pretty easy, just pip install) and the run the following command:
> $ python3 -m pytest

An advantage of using `pytest` as the test runner, it provides a much nicer output for the reader.

---

### Feature branch Tkview disclaimer
After developing a initial solution, I created a feature branch where I broken down the `BankController` into a GUIController and a `BankingHub` service class. Then I refactored the application to have a user interface using an MVC like architecture with two different implementations for the view, one using the terminal and the other using the `tkinter` package.

Since it requires additonal python packages, I decided to do it in a separate. Checkout the branch code well the gif demos here:
> https://github.com/carlosviniciusfernandes/banking_hub/tree/tkview


---
### Additional Notes
1. The python 3.7 requirement is due the use of dataclasses to write the banks's external API integrations. You can however just pip install dataclasses package  to use the application with python 3.6.
2. Since the integrations are already using dataclasses for representing balances and transaction, the `BankAccount` class are representing those entities using simple `tuples` for two reasons. First reason is that tuples are very simple to understand, behaving like immutable lists. Second reason is to let explicit that the application works with those entities (balance and transaction) in a different format from the banks.