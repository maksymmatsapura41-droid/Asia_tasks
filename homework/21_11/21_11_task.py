# Тема: Система мониторинга серверных ресурсов
# Задача:
#
# 1. Создать абстрактный класс `Metric` с метаклассом `ABCMeta` и методом `collect()`.
# 2. Реализовать классы метрик CPU, Memory, Disk через метакласс, который автоматически:
#    создает `__slots__`,
#    добавляет метод `collect()`,
#    проверяет, что значение в диапазоне 0–100.
# 3. Lобавить метрику `LoadAverage` с двумя значениями (1м и 5м), метод `collect()` возвращает среднее.
# 4. Создать класс `ServerMonitor` (`@dataclass(slots=True)`), который хранит список метрик и имеет метод `get_report()`.
# 5. Создать класс `ServerFarmMonitor` (`@dataclass(slots=True)`), который агрегирует средние значения метрик по всем серверам.
# 6. Продемонстрировать:
#    работу `__slots__` (AttributeError при добавлении нового поля),
#    полиморфизм метрик,
#    сбор отчета с одного сервера и агрегацию для фермы серверов.

from abc import ABCMeta
from dataclasses import dataclass, field

class Metric(metaclass=ABCMeta):
    __slots__ = ("name", )

    def __init__(self, name: str):
        self.name = name
    
    def collect(self):
        raise NotImplementedError("Method collect should be implemented")

class MetricFactory(ABCMeta):
    def __new__(mcs, name, bases, namespace, **kwargs):
        value_name = namespace.get('__value_name__', 'value')

        cls = super().__new__(mcs, name, bases, namespace)
        cls.__slots__ = (value_name, )

        def __init__(self, value: float):
            super(cls, self).__init__(name)
            self._validate(value)
            setattr(self, value_name, value)
        
        cls.__init__ = __init__

        def _validate(self, value):
            if not (value >= 0 and value <= 100):
                raise ValueError("Value must be in 0-100 range")

        cls._validate = _validate

        def collect(self) -> float:
            return getattr(self, value_name)
        
        cls.collect = collect

        return cls

class CpuUsage(Metric, metaclass=MetricFactory):
    __value_name__ = 'LoadAverage'

class MemoryUsage(Metric, metaclass=MetricFactory):
    __value_name__ = 'LoadAverage'

class DiskUsage(Metric, metaclass=MetricFactory):
    __value_name__ = 'LoadAverage'

@dataclass(slots=True)
class ServerMonitor:
    metrics: list = field(default_factory=list)

    def get_report(self):
        pass

@dataclass(slots=True)
class ServerFarmMonitor:
    averages: list = field(default_factory=list)

cpu1 = CpuUsage(3.2)
cpu1 = CpuUsage(5.1)
print(cpu1.collect())
print(cpu1.name)
print(cpu1.LoadAverage)
# print(cpu1.__slots__)
