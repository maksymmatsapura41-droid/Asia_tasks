class NotificationManager:
    def notify(self, type, message):
        if type == "email":
            print(f"Email: {message}")
        elif type == "sms":
            print(f"SMS: {message}")


manager = NotificationManager()
manager.notify("email", "Your order has been shipped")
manager.notify("sms", "Your order has been shipped")


# if add new channel need to change class
# Переделать систему по принципу OCP, чтобы можно было добавлять новые каналы без изменения старого кода.
# Использовать абстрактный класс / интерфейс NotificationChannel.
# Реализовать два канала (EmailChannel, SMSChannel) и показать работу.
# Добавить новый канал TelegramChannel без изменения существующих классов и показать, что он работает.
