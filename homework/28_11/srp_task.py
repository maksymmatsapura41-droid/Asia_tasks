# В приведённом классе BankAccount нарушен принцип единственной ответственности (SRP).
# Раздели обязанности класса на три отдельных компонента:
# Класс, отвечающий только за работу с балансом счёта.
# Класс, который выводит информацию о счёте.
# Класс, который отвечает за сохранение данных счёта.
# Сохрани корректное взаимодействие между классами.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

class AccountSaver():
    @staticmethod
    def save_to_db(account):
        with open ('db.txt', 'a') as file:
            file.writelines(f'{account.owner}:{account.balance}\n')

class BalanceManager():
    @staticmethod
    def deposit(account, amount=0):
        account.balance += amount

    @staticmethod
    def withdraw(account, amount=0):
        account.balance -= amount

class ShowInfo():
    @staticmethod
    def print_statement(account):
        print(f"{account.owner}: {account.balance}")

class AccountManager:
    def __init__(self):
        self.info = ShowInfo()
        self.change = BalanceManager()
        self.save_to_db = AccountSaver()

acc1 = BankAccount('Bob Smith', 100)
acc2 = BankAccount('Alice Goodenough', 150)

account_manager = AccountManager()
account_manager.info.print_statement(acc1)
account_manager.change.deposit(acc1, 5)
account_manager.info.print_statement(acc1)

account_manager.change.withdraw(acc2, 10)
account_manager.info.print_statement(acc2)

account_manager.save_to_db.save_to_db(acc1)
account_manager.save_to_db.save_to_db(acc2)
