# В данном коде отсутствует полноценное логирование.
# Необходимо добавить логи с использованием библиотеки loguru, применив как можно больше её возможностей.
# Требования к выполнению:
# Инициализировать логгер (формат, уровни, файл логов, ротация, сжатие).
# Добавить логирование в ключевые места программы с разными уровнями (debug, info, warning, error, success).
# Использовать:
# добавление контекста (bind)
# запись логов в разные файлы по уровням
# ! Здесь уже есть твой логгер, нужно переписать или, в принципе, его удалить.

import datetime
import random
from abc import ABC, abstractmethod
from pathlib import Path


class PaymentMethod(ABC):
    def __init__(self, holder: str, provider: str):
        self.holder = holder
        self.provider = provider

    @abstractmethod
    def pay(self, amount: float):
        raise NotImplementedError


class CardPayment(PaymentMethod):
    def pay(self, amount):
        if amount > 5000:
            raise ValueError("Transaction limit exceeded for card")
        print(f"{amount} paid by Card {self.provider}: {self.holder}")


class BankTransferPayment(PaymentMethod):
    def pay(self, amount: float):
        if random.random() < 0.2:
            raise ConnectionError("Bank server unavailable")
        print(f"{amount} paid by Bank Transfer {self.provider}: {self.holder}")


class CryptoPayment(PaymentMethod):
    def pay(self, amount: float):
        if amount <= 0:
            raise ValueError("Crypto amount must be positive")
        print(f"{amount} paid via Crypto {self.provider}: {self.holder}")


class PaymentLogger:
    @staticmethod
    def record_payment(payment_method: PaymentMethod, amount: float, transaction_time: str):
        log_file = Path(f"payment_log_{transaction_time[:10]}.txt")

        # Probably error
        if random.random() < 0.1:
            raise IOError("Failed to write to log file")

        with open(log_file, 'a') as file:
            file.writelines(
                f"{transaction_time};"
                f"{payment_method.holder};"
                f"{payment_method.provider};"
                f"{amount}\n"
            )


class ReceiptGenerator:
    @staticmethod
    def generate_receipt(payment_method: PaymentMethod, amount: float, transaction_time: str):
        print(
            f"=> Receipt\n"
            f"Time: {transaction_time}\n"
            f"Amount: {amount}\n"
            f"Holder: {payment_method.holder}\n"
            f"Provider: {payment_method.provider}"
        )


class PaymentService():
    def __init__(self, payment_method: PaymentMethod, amount: float, receipt: ReceiptGenerator, logger: PaymentLogger):
        self.logger = logger
        self.receipt = receipt
        self.payment_method = payment_method
        self.amount = amount
        self.transaction_time = None

    def pay(self):
        self.transaction_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Use logger catch
        self.payment_method.pay(self.amount)

        self.receipt.generate_receipt(self.payment_method, self.amount, self.transaction_time)

        self.logger.record_payment(self.payment_method, self.amount, self.transaction_time)


def run_demo():
    methods = [
        CardPayment("Alice", "Visa"),
        BankTransferPayment("Bob", "Chase"),
        CryptoPayment("Charlie", "Binance")
    ]

    for method in methods:
        amount = random.choice([50, 200, 6000, -10, 300])
        service = PaymentService(method, amount, ReceiptGenerator, PaymentLogger)

        print("\n--- New Transaction ---")
        try:
            service.pay()
        except Exception as e:
            print(f"Transaction failed: {e}")


if __name__ == "__main__":
    run_demo()
