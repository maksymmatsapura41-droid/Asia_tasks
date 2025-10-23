class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        print(f"Balance: ₹{self.balance}")

    def __update_balance(self, amount):
        self.balance += amount

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)
            self._show_balance()
        else:
            print("Invalid deposit amount!")


account = BankAccount()
account._show_balance()
account.__update_balance(500)  # Error: private method
account.deposit(500)