class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def print_statement(self):
        print(f"{self.owner}: {self.balance}")

    def save_to_db(self):
        pass
