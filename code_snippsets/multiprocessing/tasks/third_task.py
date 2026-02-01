"""
Условие:
Создать пул из 4 процессов.
Список чисел: от 10 до 50.
Каждый процесс проверяет, является ли число простым.
Главный процесс собирает результаты и выводит:
Список простых чисел
Количество простых чисел
"""

import math
from multiprocessing import Pool

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    my_list = list(range(10, 50))
    with Pool(4) as p:
        res = p.map(is_prime, my_list)

    prime_numbers = [pair[0] for pair in (zip(my_list, res)) if pair[1] is True]
    print(prime_numbers, len(prime_numbers))
    


