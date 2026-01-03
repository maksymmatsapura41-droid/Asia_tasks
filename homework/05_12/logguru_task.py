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
import sys
from abc import ABC, abstractmethod
from pathlib import Path
from loguru import logger

gl_format = "[{time:YYYY:MM:DD-HH:mm:ss}] | {name}:{line} | {level}: {message} | [tr_id={extra[transaction_id]}]"
custom_format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level> | <blue>tr_id={extra[transaction_id]}</blue>"
    )

logger.remove()
logger.add(
    "logs/info.log", 
    format=gl_format,
    level="INFO" ,
    rotation="10 kB", 
    retention="5 days",
    compression="zip",
    )

logger.add(
    "logs/error.log",
    format=gl_format,
    level="ERROR" ,
    rotation="10 kB", 
    retention="15 days",
    compression="gz",
    )

logger.add(sys.stdout, level="INFO", format=custom_format)


class PaymentMethod(ABC):
    payment_count = 0

    @classmethod
    def get_id(cls):
        cls.payment_count += 1
        return cls.payment_count

    def __init__(self, holder: str, provider: str):
        self.holder = holder
        self.provider = provider

    @logger.catch(message="Method must be implemeted", level="ERROR")
    @abstractmethod
    def pay(self, amount: float):
        logger.bind(transaction_id=id).info("Pay")
        raise NotImplementedError


class CardPayment(PaymentMethod):
    @logger.catch(message="Transaction limit exceeded for card", level="ERROR")
    def pay(self, amount):
        if amount > 5000:
            raise ValueError()
        logger.success(f"{amount} paid by Card {self.provider}: {self.holder}")

class BankTransferPayment(PaymentMethod):
    @logger.catch(message="Bank server unavailable", level="ERROR")
    def pay(self, amount: float):
        if random.random() < 0.2:
            raise ConnectionError()
        logger.success(f"{amount} paid by Bank Transfer {self.provider}: {self.holder}")


class CryptoPayment(PaymentMethod):
    @logger.catch(message="Crypto amount must be positive", level="ERROR")
    def pay(self, amount: float):
        if amount <= 0:
            raise ValueError()
        logger.success(f"{amount} paid via Crypto {self.provider}: {self.holder}")

class PaymentLogger:
    @staticmethod
    def record_payment(payment_method: PaymentMethod, amount: float, transaction_time: str):
        log_file = Path(f"payment_log_{transaction_time[:10]}.txt")
        if random.random() < 0.1:
            logger.error('Failed to record payment')

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
        if random.random() < 0.1:
            logger.warning('Failed to generate the receipt')
        logger.info(
            f"\n---- Receipt ---:\n"
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
    
    @logger.catch(message='Failed to pay', level="ERROR")
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
        id = PaymentMethod.get_id()
        with logger.contextualize(transaction_id = id):
            amount = random.choice([50, 200, 6000, -10, 300, 7000, 8000, 9000])
            service = PaymentService(method, amount, ReceiptGenerator, PaymentLogger)
            logger.info("\n--- New Transaction ---")
            try:
                service.pay()
            except Exception as e:
                logger.error(f"Transaction failed: {e}")

if __name__ == "__main__":
    run_demo()
