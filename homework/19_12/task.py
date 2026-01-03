from statistics import mean

class Server:
    def __init__(self, id, region, active, metrics, alerts):
        self.id = id
        self.region = region
        self.active = active
        self.metrics = metrics
        self.alerts = alerts

    def max_metric(self, name):
        return max(self.metrics[name])

    def avg_metric(self, name):
        return mean(self.metrics[name])
    
    # Реализовать:
    # max_metric(name) -> int
    # avg_metric(name) -> float use mean function


servers = [
    Server("srv-1", "eu", True,
           {"cpu": [30, 45, 80, 90], "memory": [60, 70, 85], "disk": [40, 50, 60]},
           ["cpu_high"]),
    Server("srv-2", "us", False,
           {"cpu": [20, 25], "memory": [30, 35], "disk": [70, 80, 90]},
           []),
    Server("srv-3", "eu", True,
           {"cpu": [95, 92, 88], "memory": [90, 85], "disk": [50, 55]},
           ["cpu_high", "memory_high"]),
    Server("srv-4", "us", True,
           {"cpu": [95, 92, 88], "memory": [90, 85], "disk": [50, 55]},
           [])           
]

'''
Задания
1.--------------------------------------------
Получить список строк id серверов,
у которых active == True и region == "eu".
'''
active_eu = list(item.id for item in filter(lambda x: x.active == True and x.region == "eu", servers))
print(active_eu)
'''
2.--------------------------------------------
Получить список кортежей вида:
(id, max_cpu)
где max_cpu — максимальное значение метрики cpu сервера.
'''
all_with_max_cpu = list(map(lambda x: (x.id, x.max_metric("cpu")), servers))
print(all_with_max_cpu)
'''
3.--------------------------------------------
Получить список id серверов,
у которых максимальное значение cpu строго больше 90.
'''
cpu_result = list(item.id for item in filter(lambda x: x.max_metric("cpu") > 90, servers))
print(cpu_result)

'''
4.--------------------------------------------
Создать generator expression,
который последовательно возвращает все значения cpu
по всем серверам.
'''
print("GENERATOR-N4")
gen_get_cpu = (cpu_value for server in servers for cpu_value in server.metrics["cpu"] )
for item in range(sum(len(server.metrics["cpu"]) for server in servers)):
    print(next(gen_get_cpu))
print('-------------')
'''
5.--------------------------------------------
Создать генератор, возвращающий кортежи вида:
(id, metric_name, value)
для всех метрик всех серверов,
где value >= 85.
'''
print("GENERATOR-N5")
# def get_metric(servers: list):
#     for server in servers:
#         for key, values in server.metrics.items():
#             for value in values:
#                 if value >= 85:
#                     yield (server.id, key, value)

gen_get_metric = ((server.id, k, v) for server in servers for k, values in server.metrics.items() for v in values if v >= 85)
for item in range(len([v for server in servers for metric in server.metrics.values() for v in metric if v >= 85])):
    print(next(gen_get_metric))
print('--------------')
        
'''
6.--------------------------------------------
Отсортировать список серверов по двум критериям:
количеству алертов (по убыванию)
максимальному значению cpu (по убыванию)
Использовать одну lambda в параметре key.
'''
double_sorted = list(f'{item.id}:{item.max_metric("cpu")}' for item in sorted(servers, reverse=True, key=lambda x: (len(x.alerts), x.max_metric("cpu"))))
print(double_sorted)
'''
7.--------------------------------------------
Отсортировать серверы
по среднему значению метрики memory
в порядке убывания.
'''
mem_result = list(item.id for item in sorted(servers, reverse=True, key=lambda x: x.avg_metric("memory")))
print(mem_result)
'''
8.--------------------------------------------
С помощью functools.partial создать функции:
is_cpu_critical с порогом 90
is_memory_warning с порогом 80
'''
from functools import partial

def is_metric_above_threshold(metric_name: str, threshold: int, server: Server):
    return server.max_metric(metric_name) >= threshold

is_cpu_critical = partial(is_metric_above_threshold, "cpu", 90)
is_memory_warning = partial(is_metric_above_threshold, "memory", 80)

for item in servers:
    print(item.id, 'is_cpu_critical:', is_cpu_critical(item))
    print(item.id, 'is_memory_warning:', is_memory_warning(item))