'''
1. ООП-структура
Создай класс DataProcessor, который:
принимает в конструкторе размер набора данных;
генерирует список случайных целых чисел;
содержит метод process_value(x), который выполняет вычисление над числом
(например: x ** 2 + x).

2. Асинхронная обработка (Pool.apply_async)
Создай multiprocessing.Pool;
Для каждого элемента данных запусти задачу через apply_async;
Собери результаты с помощью объектов AsyncResult (get()). (смотри help.py)

Обязательно:
используй callback или error_callback;  (смотри help.py)
корректно закрой пул (close, join).

3. Взаимодействие процессов (Pipe)

Реализуй функцию-процесс collector:
принимает данные через Pipe;
вычисляет агрегированное значение (сумма, например);
отправляет результат обратно через Pipe.

Главный процесс должен:
передать обработанные данные в дочерний процесс;
получить и вывести итоговый результат.
'''

from random import randint
from multiprocessing import Pool, Pipe, Process

class DataProcessor:
    def __init__(self, size: int):
        self.size = size

    def create_random_list(self):
        return [randint(1, 10) for _ in range(self.size)]
    
    @staticmethod
    def process_value(x):
        return x ** 2 + x

def collector(conn):
    received_data = conn.recv()
    conn.send(sum(received_data))
    conn.close()

# Success result
def on_success(result):
    print(f"Success: {result}")

# Result with error
def on_error(error):
    print(f"Error: {error}")

if __name__ == '__main__':
    dp = DataProcessor(5)
    data = dp.create_random_list()
    async_results = []
    results = []
    with Pool(processes=3) as pool:
        for item in data:
            async_process = pool.apply_async(
                dp.process_value,
                args=(item, ),
                callback=on_success,
                error_callback=on_error
            )
            async_results.append(async_process)
        
        pool.close()
        pool.join()

    for item in async_results:
        try:
            result = item.get(timeout=2)
            results.append(result)
        except Exception as e:
            raise("The error happend retrieving result:", e)
    
    print("Final results: ", results)

    conn1, conn2 = Pipe()
    p1 = Process(target=collector, args=(conn2,))
    p1.start()
    print('Sending data to pipe:', results)
    conn1.send(results)
    modifyied_data = conn1.recv()
    conn1.close()
    p1.join()
    print('Received modified data from pipe:', modifyied_data)