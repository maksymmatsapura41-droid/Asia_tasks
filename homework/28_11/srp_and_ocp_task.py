# Реализуй систему обработки платежей так, чтобы она соответствовала принципам SRP и OCP.

# SRP (Single Responsibility Principle):
# -Каждый класс выполняет только одну функцию:
# -классы оплаты отвечают только за проведение платежа,
# -логгер - за логирование,
# -генератор квитанций - за создание квитанции,
# -сервис - за управление процессом.

# OCP (Open/Closed Principle):
# Должно быть возможно добавить новый способ оплаты, создав новый класс,
# не изменяя существующий код PaymentService.

# Детали:
# Создай интерфейс PaymentMethod с методом pay(amount).
# Реализуй несколько способов оплаты: например, CardPayment, BankTransferPayment.
# Сделай отдельные классы:
# PaymentLogger - логирование,
# ReceiptGenerator - квитанции,
# PaymentService - управление процессом.
# PaymentService должен принимать любой PaymentMethod и работать без изменений при добавлении новых способов оплаты.

from abc import ABC, abstractmethod
from dataclasses import field, dataclass
import datetime

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        raise NotImplementedError
    
class CardPayment(PaymentMethod):
    def __init__(self, card_holder, card_name):
        self.card_holder = card_holder
        self.card_name = card_name

    def pay(self, amount):
        print(f'{amount} paid by Card {self.card_name}: {self.card_holder}')

class BankTransferPayment(PaymentMethod):
    def __init__(self, account_holder, bank_name):
        self.account_holder = account_holder
        self.bank_name = bank_name

    def pay(self, amount):
        print(f'{amount} paid by Bank Transfer {self.bank_name}: {self.account_holder}')


class PaymentLogger:
    @staticmethod    
    def record_payment(payment_data):
        with open('paymenet_log.txt', 'a') as file:
            print(f'{datetime.time}:{payment_data.amount}')
            file.writelines(f'{datetime.time}:{payment_data.amount}')

class ReceiptGenerator:
    @staticmethod
    def generate_receipt(payment_data):
        print(f'Receipt:{datetime.time}:{payment_data.amount}:')
        

class PaymentService(ReceiptGenerator, PaymentLogger):
    @staticmethod
    def pay(payment_data):
        payment_data.pay(payment_data.amount)

service = PaymentService()
card = CardPayment('Alice Superstar', 'Visa')
card.pay(30)

transfer = BankTransferPayment('Bob Goodnight', 'Santander')
transfer.pay(40)
service(card)
