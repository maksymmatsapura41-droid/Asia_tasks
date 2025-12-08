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
import datetime
from time import sleep

class PaymentMethod(ABC):
    def __init__(self, holder: str, provider: str):
        self.holder = holder
        self.provider = provider
        
    @abstractmethod
    def pay(self, amount: float):
        raise NotImplementedError
    
class CardPayment(PaymentMethod):
    def __init__(self, holder: str, provider: str):
        super().__init__(holder, provider)

    def pay(self, amount):
        print(f'{amount} paid by Card {self.provider}: {self.holder}')

class BankTransferPayment(PaymentMethod):
    def __init__(self, holder: str, provider: str):
        super().__init__(holder, provider)

    def pay(self, amount: float):
        print(f'{amount} paid by Bank Transfer {self.provider}: {self.holder}')

class PaymentLogger:
    @staticmethod    
    def record_payment(payment_method: PaymentMethod, amount: float, transaction_time: str):
        with open(f'paymenet_log_{transaction_time}.txt', 'a') as file:
            file.writelines(f'{transaction_time}:{payment_method.holder}:{payment_method.provider}:{amount}\n')

class ReceiptGenerator:
    @staticmethod
    def generate_receipt(payment_method: PaymentMethod, amount: float, transaction_time: str):
        print(f'=> Receipt\nTime: {transaction_time}\nAmount: {amount}\nHolder: {payment_method.holder}\nProvider: {payment_method.provider}')

class PaymentService():
    def __init__(self, payment_method: PaymentMethod, amount: float, receipt: ReceiptGenerator, logger: PaymentLogger, ):
        self.logger = logger
        self.receipt = receipt
        self.payment_method = payment_method
        self.amount = amount
        self.transaction_time = None
    
    def pay(self):
        self.transaction_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.payment_method.pay(self.amount)
        self.receipt.generate_receipt(self.payment_method, self.amount, self.transaction_time)
        self.logger.record_payment(self.payment_method, self.amount, self.transaction_time)
    
logger = PaymentLogger()
receipt = ReceiptGenerator()
card = CardPayment('Alice Superstar', 'Visa')

card_service = PaymentService(card, 30, receipt, logger)
card_service.pay()

sleep(15)
transfer = BankTransferPayment('Bob Goodnight', 'Santander')
transfer_service = PaymentService(transfer, 50, receipt, logger)
transfer_service.pay()

