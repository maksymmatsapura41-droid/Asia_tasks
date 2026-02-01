import multiprocessing
from multiprocessing import shared_memory
import struct
import time


def increment_task(shm_name, lock, iterations):
    # Подключаемся к существующей памяти
    existing_shm = shared_memory.SharedMemory(name=shm_name)

    for _ in range(iterations):
        with lock:
            # 1. Читаем 4 байта (целое число 'i')
            current_value = struct.unpack('i', existing_shm.buf[:4])[0]

            # 2. Инкрементируем
            new_value = current_value + 1

            # 3. Записываем обратно
            struct.pack_into('i', existing_shm.buf, 0, new_value)

    existing_shm.close()


if __name__ == "__main__":
    # Выделяем 4 байта под одно целое число (int - 'i')
    shm = shared_memory.SharedMemory(create=True, size=4)

    # Инициализируем нулем
    struct.pack_into('i', shm.buf, 0, 0)

    lock = multiprocessing.Lock()
    total_updates = 5000

    # Запускаем два параллельных процесса
    p1 = multiprocessing.Process(target=increment_task, args=(shm.name, lock, total_updates))
    p2 = multiprocessing.Process(target=increment_task, args=(shm.name, lock, total_updates))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # Проверяем результат
    final_result = struct.unpack('i', shm.buf[:4])[0]
    print(f"Ожидалось: {total_updates * 2}")
    print(f"Результат в Shared Memory: {final_result}")

    shm.close()
    shm.unlink()