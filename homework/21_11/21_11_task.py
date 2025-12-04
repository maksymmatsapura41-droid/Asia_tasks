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
from statistics import mean

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
        cls.__slots__ = (value_name,)

        def __init__(self, value: tuple):
            super(cls, self).__init__(name)

            if isinstance(value, tuple):
                for item in value:
                    self._validate(item)
                setattr(self, value_name, value)
            else:
                self._validate(value)
                setattr(self, value_name, (value,))
        
        cls.__init__ = __init__

        def _validate(self, value):
            if not (value >= 0 and value <= 100):
                raise ValueError("Value must be in 0-100 range")

        cls._validate = _validate

        def collect(self) -> float:
            return mean(getattr(self, value_name))
        cls.collect = collect
        return cls

class CpuUsage(Metric, metaclass=MetricFactory):
    __slots__ = ("CPUUsage",)
    __value_name__ = 'CPUUsage'

class MemoryUsage(Metric, metaclass=MetricFactory):
    __slots__ = ("MemUsage",)
    __value_name__ = 'MemUsage'

class DiskUsage(Metric, metaclass=MetricFactory):
    __slots__ = ("DiskUsage",)
    __value_name__ = 'DiskUsage'

class LoadAverage(Metric, metaclass=MetricFactory):
    __slots__ = ("LoadAverage",)
    __value_name__ = 'LoadAverage'

@dataclass(slots=True)
class ServerMonitor:
    metrics: list = field(default_factory=list)

    def get_report(self):
        report = {}
        for metric in self.metrics:
            report.setdefault(metric.name, []).append(metric.collect())
        return report

@dataclass(slots=True)
class ServerFarmMonitor:
    averages: list = field(default_factory=list)

load = LoadAverage((3.2, 5.1))
# print(load.__slots__)
print(load.name)
print(load.LoadAverage)
# print(load.collect())
cpu_util = CpuUsage(50)
cpu_util.cores = 4  # AttributeError: 'CpuUsage' object has no attribute 'cores' and no __dict__ for setting new attributes
# print(cpu_util.__slots__)

server1 = ServerMonitor([
            LoadAverage((3.2, 5.1)),
            CpuUsage(90),
            MemoryUsage(30),
            DiskUsage(10)
        ])

print(server1.get_report())

server2 = ServerMonitor([
            LoadAverage((1.2, 2.2)),
            CpuUsage(10),
            MemoryUsage(60),
            DiskUsage(40)
        ])


server_farm1 = ServerFarmMonitor([server1.get_report(), server2.get_report()])
print(server_farm1.averages)

