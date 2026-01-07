'''
Есть функция process_data(n), которая суммирует числа от 1 до n:
Задача: написать и применить декораторы:
@log_time – измеряет и выводит в консоль время выполнения функции.
@log_memory – выводит приблизительное потребление памяти функцией.
( Узнать потребление памями:
  result = func(*args, **kwargs)
  size = sys.getsizeof(result)
)
@log_exceptions – при возникновении ошибки записывает её в файл errors.log и повторно поднимает исключение.
Примени все декораторы одновременно к process_data и протестируйте их (n = 1000000).
'''
import time
import sys
import traceback
import functools

def process_data(n):
    result = 0
    for i in range(n):
        result += i
    return result
