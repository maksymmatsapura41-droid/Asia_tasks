# 1.
# Асинхронный Health Check микросервисов
# Контекст:
# Тебе нужно проверить доступность 50 сервисов. Делать это последовательно - слишком долго.
# Задание:
# Используй библиотеку aiohttp.
# Создай список из 5–10 URL-адресов (можно взять реальные, например https://google.com, или локальные http://localhost:8080).
# Напиши асинхронную функцию check_url(session, url), которая выполняет GET-запрос и возвращает статус-код.
# Усложнение:
# Добавь таймаут 2 секунды на каждый запрос.
# Если сервис не отвечает - возвращай статус "Timeout/Error".
# В конце выведи финальный отчет: какие сервисы UP (200), а какие DOWN
import aiohttp
import asyncio

async def check_url(session, url):
    try:
        async with session.get(url, timeout=2) as response:
            # print(await response.text())
            return url, response.status
    except asyncio.TimeoutError:
        return url, "Timeout/Error"
    except Exception as e:
        return url, str(e)

async def main():
    urls = ["https://google.com", "https://github.com", "https://python.org", "https://non-existing-url.example"]
    async with aiohttp.ClientSession() as session:
        tasks = [check_url(session, url) for url in urls]
        result = await asyncio.gather(*tasks)
        print(*result)

#2
# Параллельное выполнение команд на серверах (SSH-имитация)
# Контекст:
# Тебе нужно обновить пакет или собрать логи с 10 разных нод одновременно.
# Задание:
# Напиши функцию run_remote_command(server_name, command).
# Вместо реального SSH используй asyncio.sleep() со случайным временем (от 1 до 4 секунд), чтобы имитировать сетевую задержку.
# Каждая функция должна возвращать Лог выполнения (например:
# [Server-01]: Output of 'df -h'...).
# Используй asyncio.as_completed, чтобы выводить результат каждого сервера сразу, как только он пришёл, не дожидаясь самого медленного сервера.
import random

async def run_remote_command(server_name, command):
    timeout = random.randint(1, 4)
    await asyncio.sleep(timeout)
    return f"[{timeout}]: {server_name}: Output of {command}"

async def main_1():
    servers = ["prod-db-01", "prod-web-01", "prod-cache-01"]
    commands = ['df -h', 'rm -rf /tmp/*', 'top']
    tasks = [run_remote_command(server, command) for server, command in zip(servers, commands)]
    for task in asyncio.as_completed(tasks):
        print(await task)


# 3 Асинхронный ротатор логов с ограничением (Semaphores)
# 
# Контекст:
# Тебе нужно сжать (gzip) 100 гигабайтных логов. Если запустить все 100 процессов одновременно - сервер умрёт 
# от нагрузки на CPU/Disk.
# Задание:
# Создай очередь задач (имена файлов логов).
# Напиши функцию-воркер compress_log(file_name).
# Используй asyncio.Semaphore(3), чтобы ограничить количество одновременных сжатий до трёх.
# Программа должна брать следующий файл из очереди только тогда, когда один из трёх предыдущих освободил место.
# Выводи сообщение:
# "Сейчас обрабатывается [File], в очереди осталось [N]".


semaphore = asyncio.Semaphore(3)

async def compress_log(file_name):
    async with semaphore:
        duration = random.randint(1,5)
        print(f"Сейчас обрабатывается [{file_name}]")
        await asyncio.sleep(duration)
    
async def main_2():
    logs = [f'access_log_{i}.json' for i in range(20)]
    tasks = [compress_log(file_name) for file_name in logs]
    total = len(logs)
    completed = 0
    # await asyncio.gather(*tasks)
    for task in asyncio.as_completed(tasks):
        await task
        completed += 1
        print(f"Осталось обработать {total - completed}")

if __name__ == "__main__":
    asyncio.run(main_2())