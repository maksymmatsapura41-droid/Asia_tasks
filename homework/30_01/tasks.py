# Задача 1
#
# Условие: Представь, что ты пишешь софт для умного дома. Тебе нужно одновременно запустить три устройства:
# Кофемашина: варит кофе 3 секунды.
# Чайник: кипятит воду 5 секунд.
# Тостер: жарит хлеб 2 секунды.
#
# Твоя задача:
# Напиши асинхронную функцию для каждого устройства.
# Запусти их одновременно (конкурентно).
# Используй asyncio.gather, чтобы дождаться завершения всех приборов и вывести общее время работы программы.
import asyncio, time

async def coffee_machine(duration: int = 3):
    print("Start making coffee...")
    await asyncio.sleep(duration)
    print(f"Finish making coffee {duration}s.")

async def kettle(duration: int = 5):
    print("Start boiling water...")
    await asyncio.sleep(duration)
    print(f"Finish boiling water {duration}s.")

async def toaster(duration: int = 2):
    print('Start making toast...')
    await asyncio.sleep(duration)
    print(f'Finish making toast {duration}s.')

async def main():
    start = time.time()
    await asyncio.gather(coffee_machine(), kettle(), toaster())
    end = time.time()
    print(str(end - start))

if __name__ == "__main__":
    asyncio.run(main())
# Задача 2:
#
# Условие: Ты пишешь загрузчик файлов. У тебя есть список из 5 файлов (просто строки с названиями).
# Функция download_file(name) имитирует загрузку случайное время (от 1 до 4 секунд) и возвращает размер файла (например, len(name) * 100).
# В основной функции main ты должен запустить загрузку всех файлов через создание объектов Task.
# Пока файлы "качаются", программа должна вывести в консоль сообщение: "Главный поток не заблокирован, могу делать что-то еще!".
# В конце нужно собрать все размеры файлов и вывести их сумму.
# Ключевой момент: Не используй gather в этой задаче. Используй список тасок и пройдись по ним в цикле с await.
import random

file_names = [ f'File-{str(random.randint(1, 10))}' for _ in range(5)]
print(file_names)

async def download_file(name: str) -> int:
    duration = random.randint(1, 10)
    print(f'Downloading file {name}...')
    await asyncio.sleep(duration)
    file_size = len(name) * duration
    print(f'Downloaded file {name} in {duration}s, size {file_size}')
    return file_size

async def main():
    start = time.time()
    tasks = [asyncio.create_task(download_file(name)) for name in file_names]
    print('Tasks:', len(tasks))
    total_size = []
    print("Главный поток не заблокирован, могу делать что-то еще!")
    for task in tasks:
        total_size.append(await task)

    end = time.time()
    print(f'Total time: {str(end - start)} Total size: {sum(total_size)}')

if __name__ == "__main__":
    asyncio.run(main())
