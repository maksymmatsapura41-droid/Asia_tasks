# Проблема добавить новый способ связи
# Переделать систему по принципу OCP, чтобы можно было добавлять новые каналы без изменения старого кода.
# Использовать абстрактный класс
# Реализовать два канала (EmailChannel, SMSChannel) и показать работу.
# Добавить новый канал TelegramChannel без изменения существующих классов и показать, что он работает.


from abc import ABC, abstractmethod
from dataclasses import dataclass, field

class MediaChannel(ABC):
    @abstractmethod
    def notify(self, message):
        pass

class EmailChannel(MediaChannel):

    def notify(self, message):
        print(f"Email: {message}")
        
class SMSChannel(MediaChannel):

    def notify(self, message):
        print(f"SMS: {message}")

class TelegramChannel(MediaChannel):

    def notify(self, message):
        print(f"Telegram: {message}")

@dataclass
class NotificationManager:
    channels: list = field(default_factory=list)

    def notify(self, message):
        for channel in self.channels:
            channel.notify(message)

manager = NotificationManager([EmailChannel(), SMSChannel(), TelegramChannel()])
manager.notify("Your order has been shipped")
