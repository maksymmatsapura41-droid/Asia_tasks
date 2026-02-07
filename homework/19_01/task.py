# Есть автоматизированный склад. У нас есть Главный Контроллер (основной процесс) и 5 Роботов-манипуляторов (дочерние процессы). 
# Роботы должны выполнить работу и отчитаться в общую память.
# Цель - реализовать следующие механизмы:
# 1. Авторизация через shared_memory
# Главный процесс записывает в общую память строку-пароль (например, "SERVER_77").
# Каждый робот должен подключиться к этому сегменту памяти по его уникальному имени, прочитать пароль и вывести его на экран.
# 2. Общий счетчик через Value
# Создай общую переменную целого типа ('i').
# Каждый раз, когда робот «берет заказ», он должен прибавить к этому счетчику 1.
# 3. Синхронизация через Lock (Предотвращение хаоса)
# Создай объект блокировки.
# Операция counter.value += 1 состоит из трех шагов (чтение, сложение, запись). 
# Чтобы два робота не перезаписали данные друг друга одновременно, оберни этот процесс в lock.
# 4. Карта склада через Array
# Создай массив из 5 элементов (по числу роботов).
# Каждый робот по завершении работы должен найти в массиве ячейку со своим индексом и заменить в ней 0 на 1.
# 5. Общий лог через Manager (Высокий уровень)
# Через multiprocessing.Manager() создай общий список (list).
# В конце работы робот добавляет в этот список сложный объект — словарь, например: {"id": robot_id, "time": "12:00"}.
#
# Чек-лист для реализации (Алгоритм):
# В начале:
# Создай Value для счетчика и Array для статусов.
# Инициализируй Manager и его список.
# Создай блок shared_memory, запиши туда байты.
# Запуск:
# В цикле создай 5 процессов Process. Передай все созданные объекты в аргументы (args).
# Запусти процессы (.start()).
# Внутри функции робота:
# Подключись к shared_memory по имени.
# Выполни действия с счетчиком и массивом (не забывай про Lock).
# Добавь запись в список менеджера.
# Закрой доступ к shared_memory (.close()).
# Завершение:
# Дождись всех роботов через .join().
# Выведи финальные результаты: значение счетчика, состояние массива и все записи из лога.
# Важно: Очисти память shm.unlink().
#
# Подсказка по типам данных (ctypes):
# При создании Value и Array используй коды типов:
# 'i' - целое число (integer).
# 'd' - число с плавающей точкой (double).
# 'b' - булево значение или байт.

from multiprocessing import shared_memory, Value, Array, Lock, Process, Manager
import struct, datetime, time


def robot_function(id, mem_name, counter, warehouse, final_log, lock):
    existing_shm = shared_memory.SharedMemory(name=mem_name)
    read_password(id, existing_shm)
    order_id = take_order(id, counter, lock)
    complete_order(id, warehouse, order_id)
    report(id, final_log, order_id)
    existing_shm.close()

def report(id, final_log, order_id):
    time.sleep(1)
    end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'{id} reported completed order at {end_time}')
    final_log.append({'id': id, 'end_time': end_time, 'order_id': order_id})

def read_password(id, existing_shm):
    current_password = (struct.unpack('9s', existing_shm.buf[:9])[0]).decode()
    print(f'Robot {id} read', current_password)

def take_order(id, counter, lock):
    with lock:
        counter.value += 1
        current_value = counter.value
        print(f'Robot {id} took order', counter.value)
        time.sleep(1)
    return current_value

def complete_order(id, warehouse, order_id):
    warehouse[id] = order_id
    print(f'Robot {id} completed order', warehouse[id])

if __name__ == '__main__':
# Для ASCII латиница имеет размер 1 байт. Но если ты хочешь автоматически определять размер, можно использовать примерно такой формат:
# Здесь есть также нюанс с памятью - при создании shared_memory память выделяется страницами (page), 
# которые, как правило, по 4 КБ, поэтому можно смело выделять 100 и больше байт в этом случае.
    
    server_id = "SERVER_77".encode('utf-8') # здесь важно сначала превратить строку в байты
    data_len = len(server_id)
    fmt = f"{data_len}s"
    size = struct.calcsize(fmt)
    shm_name = shared_memory.SharedMemory(create=True, size=size)
    struct.pack_into('9s', shm_name.buf, 0, server_id)
    
    counter = Value('i', 0)
    warehouse = Array('i', [0, 0, 0, 0, 0])
    lock = Lock()
    with Manager() as manager:
        final_log = manager.list()
        processes = [Process(target=robot_function, args=(id, shm_name.name, counter, warehouse, final_log, lock)) for id in range(5)]
        for p in processes: p.start()
        for p in processes: p.join()
        print(f'Total orders: {counter.value}\n', f'Completed orders: {list(warehouse)}\n', final_log)
    shm_name.unlink()



