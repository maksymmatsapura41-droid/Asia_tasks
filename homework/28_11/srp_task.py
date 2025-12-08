# В приведённом классе BankAccount нарушен принцип единственной ответственности (SRP).
# Раздели обязанности класса на три отдельных компонента:
# Класс, отвечающий только за работу с балансом счёта.
# Класс, который выводит информацию о счёте.
# Класс, который отвечает за сохранение данных счёта.
# Сохрани корректное взаимодействие между классами.


class BankAccount:
    def __init__(self, owner: str, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount=0):
        self.balance += amount

    def withdraw(self, amount=0):
        self.balance -= amount        

class AccountSaver():
    @staticmethod
    def save_to_db(account: BankAccount):
        with open ('db.txt', 'a') as file:
            file.writelines(f'{account.owner}:{account.balance}\n')

class ShowInfo():
    @staticmethod
    def print_statement(account: BankAccount):
        print(f"{account.owner}: {account.balance}")

acc1 = BankAccount('Bob Smith', 100)
acc2 = BankAccount('Alice Goodenough', 150)

ShowInfo.print_statement(acc1)
acc1.deposit(5)
ShowInfo.print_statement(acc1)
acc2.withdraw(10)
ShowInfo.print_statement(acc2)
AccountSaver.save_to_db(acc1)
AccountSaver.save_to_db(acc2)
