"""
Условие:
Создать 4 процесса, каждый генерирует 10 случайных чисел.
Записать все числа в Queue.
Главный процесс подсчитывает сумму всех чисел.
--------------------------------------------------------------------
Условие:
Создать 3 процесса, каждый генерирует 15 случайных чисел от 1 до 200.
Передавать числа в Queue.
Главный процесс находит максимальное число среди всех.
"""

from multiprocessing import Process, Queue
import random

def gen_random_numbers(q, start: int = 0, stop: int = 10, total: int = 10):
    q.put([random.randint(start, stop) for _ in range(total)])

if __name__ == "__main__":
    q1 = Queue()
    processes = [Process(target=gen_random_numbers, args=(q1,)) for _ in range(4)]
    for p in processes:
        p.start()
        p.join()

    res = []
    while not q1.empty():
        res.extend(q1.get())
    print('Task1:', sum(res), res)

    q2 = Queue()
    processes2 = [Process(target=gen_random_numbers, args=(q2, 1, 200, 15)) for _ in range(3)]
    for p in processes2:
        p.start()
        p.join()
    
    res2 = []
    while not q2.empty():
        res2.extend(q2.get())
    print('Task2:', max(res2), res2)
