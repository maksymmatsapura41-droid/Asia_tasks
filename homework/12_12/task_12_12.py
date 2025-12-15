# Есть список серверов:
# Функции, которые нужно написать:
#   Функция для классификации нагрузки сервера
#   Принимает количество запросов (requests)
#   Возвращает строку "high", "medium" или "low"
#   >1000 - high
#   >500 and <1000 - medium
#   <500 - low

def load(requests: int):
    if requests > 1000:
        return 'high'
    elif requests < 500:
        return 'low'
    return 'medium'

#   Функция для проверки состояния сервера (healthy)
#   Принимает словарь с информацией о сервере
#   Возвращает True, если сервер онлайн и количество ошибок небольшое (<10), иначе False

def healthy(info: dict):
    if info['status'] == 'online' and info['errors'] < 10:
        return True
    return False

# Задачи (выполнять через comprehensions)

# Создать список строк вида "server-1: high load", используя функцию классификации нагрузки. 
# Учитывать только online-серверы.

# Создать словарь, где ключ — имя сервера, а значение — результат функции проверки состояния. 
# Учитывать только online-серверы.

# Создать множество регионов, где есть нездоровые серверы.
# Создать словарь, где ключ — регион, а значение — список серверов с высокой нагрузкой (high load).

servers = [
    {"name": "server-1", "status": "online", "requests": 1200, "errors": 5, "region": "EU"},
    {"name": "server-2", "status": "offline", "requests": 0, "errors": 0, "region": "US"},
    {"name": "server-3", "status": "online", "requests": 950, "errors": 15, "region": "EU"},
    {"name": "server-4", "status": "online", "requests": 400, "errors": 2, "region": "ASIA"},
    {"name": "server-5", "status": "offline", "requests": 0, "errors": 0, "region": "EU"},
]

result1 = [record["name"] +': high load' for record in servers if load(record['requests']) == 'high' and healthy(record)]
print(result1)

result2 = {record["name"]:healthy(record) for record in servers if healthy(record)}
print(result2)

result3 = set(record["region"] for record in servers if not healthy(record))
print(result3)

result4 = {record["region"]:[item["name"] for item in servers if load(item["requests"]) == 'high' and item["region"] == record["region"]] for record in servers}
print(result4)
