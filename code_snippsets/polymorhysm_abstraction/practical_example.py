from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Payed {amount} usd by card")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Payed {amount} usd by PayPal")

def process_payment(payment: Payment, amount: float):
    payment.pay(amount)

process_payment(CreditCardPayment(), 100)
process_payment(PayPalPayment(), 250)
