class PaymentProcessor:
    def process_payment(self, country, method, amount):
        if country == "US":
            if method == "credit_card":
                print(f"Processing {amount} USD by credit card with US rules")
            elif method == "paypal":
                print(f"Processing {amount} USD by PayPal with US rules")
        elif country == "DE":
            if method == "credit_card":
                print(f"Processing {amount} EUR by credit card with DE rules")
            elif method == "paypal":
                print(f"Processing {amount} EUR by PayPal with DE rules")

# Переписать существующую систему обработки платежей так, чтобы новые страны и методы оплаты можно было добавлять без изменения существующего кода.
# Создать абстрактный класс PaymentMethod с методом pay(amount: float) для реализации разных способов оплаты.
# Создать абстрактный класс CountryRules с методом apply_rules(amount: float) для применения правил оплаты в разных странах (например, налоги, комиссии).
# Реализовать конкретные методы оплаты:
# CreditCard
# PayPal
# Каждый из них принимает объект CountryRules и использует его для расчета финальной суммы.
# Реализовать конкретные правила для стран:
# USRules
# DERules
# Продемонстрировать работу системы, создав комбинации метода оплаты и правил страны и вызвав pay(amount).
# Дополнительно: добавить новый метод оплаты или новые правила для другой страны, не меняя существующие классы, и показать, что это работает.без изменения существующих классов и показать, что это работает.