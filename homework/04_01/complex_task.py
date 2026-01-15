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

def log_time(funct):
    @functools.wraps(funct)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        funct_result = funct(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'Execution took {run_time:.4f} secs')
        return funct_result
    return wrapper

def log_memory(funct):
    @functools.wraps(funct)
    def wrapper(*args, **kwargs):
        funct_result = funct(*args, **kwargs)
        size = sys.getsizeof(funct_result)
        print(f'Approximate memory usage: {size}')
        return funct_result
    return wrapper

def log_exceptions(funct):
    @functools.wraps(funct)
    def wrapper(*args, **kwargs):
        try:
           funct_result = funct(*args, **kwargs)
           return funct_result
        except Exception as e:
            with open('repos/Asia_tasks/homework/04_01/traceback.log', 'a') as log_file:
                traceback.TracebackException.from_exception(e).print(file=log_file)
                raise e
    return wrapper

@log_time
@log_memory
@log_exceptions
def process_data(n):
    result = 0
    for i in range(n):
        result += i
    return result

process_data(1000000)
