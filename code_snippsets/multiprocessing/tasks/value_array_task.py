# Суть: Один процесс должен подготовить данные, а второй - обработать их, используя
# Array как общую рабочую область и Value как сигнал готовности.
#
# Задание:
# Создай multiprocessing.Array (тип 'i' - целые числа) на 10 элементов, заполненный нулями.
# Создай multiprocessing.Value (тип 'b' - boolean/истина-ложь), изначально False.
# Напиши два процесса:
# Процесс-Заполнитель (Writer): записывает в массив числа от 1 до 10 и после этого меняет Value на True.
# Процесс-Читатель (Reader): в цикле while проверяет Value. Как только оно стало True,
# он выводит сумму элементов массива на экран и завершается.
# Запусти их одновременно. + Используй sleep для имитации долгой работы.

import multiprocessing
import time


def writer(array_to_change, flag):
    print("Start array changing")
    for i in range(len(array_to_change)):
        
        array_to_change[i] = i + 1
        time.sleep(0.2)
    flag.value = True
    print('Finish array changing')
    

def reader(my_array, flag):
    print("Start reading")
    while not flag.value:
        time.sleep(0.2)
    print(sum(my_array))
    


if __name__ == "__main__":
    my_array = multiprocessing.Array('i', 10)
    flag = multiprocessing.Value('b', False)
    

    p1 = multiprocessing.Process(target=writer, args=(my_array, flag))
    p2 = multiprocessing.Process(target=reader, args=(my_array, flag))
    
    p2.start()
    p1.start()

    p1.join()
    p2.join()
