from multiprocessing import Process, Lock, Value


def increment(shared_value, lock):
    for _ in range(10000):
        with lock:
            # Без lock здесь возникнет race condition
            shared_value.value += 1


if __name__ == '__main__':
    # Общее число в разделяемой памяти
    counter = Value('i', 0)
    lock = Lock()

    processes = [Process(target=increment, args=(counter, lock)) for _ in range(5)]

    for p in processes: p.start()
    for p in processes: p.join()

    print(f"Итоговое значение: {counter.value}")


'''
With lock
[ acquire lock ]
read total
+1
write total
[ release lock ]

Without Lock less
P0: read 100
P1: read 100
P2: read 100
P3: read 100
P4: read 100

After 5 adding 101 (105 expected)
'''