"""Условие

Реализуйте программу с использованием модуля multiprocessing, в которой:
Главный процесс создаёт Pipe.
Дочерний процесс (worker):
формирует список чисел от 1 до 10;
отправляет этот список в главный процесс через Pipe;
закрывает соединение.
Главный процесс:
получает список чисел через Pipe;
дожидается завершения дочернего процесса.
После получения данных главный процесс создаёт Pool из 3 процессов.
С помощью Pool главный процесс параллельно:
вычисляет квадрат каждого числа из полученного списка.
Главный процесс собирает результаты и выводит итоговый список в консоль.
"""

from multiprocessing import Pool, Pipe, Process

def worker(conn):
    conn.send(list(range(1, 11)))
    conn.close()

def square(x):
    return x*x

if __name__ == "__main__":
    parent_side, worker_side = Pipe()
    p = Process(target=worker, args=(worker_side,))
    p.start()
    msg = parent_side.recv()
    p.join()

    with Pool(3) as pool:
        pool_res = pool.map(square, msg)

    print(pool_res)

