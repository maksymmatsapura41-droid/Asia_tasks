from multiprocessing import Process, Value, Array, Lock

def update_data(n, arr, lock, true_flag):
    with lock: # Обязательно защищаем доступ
        for _ in range(10000):
            n.value += 1.5
            if n.value >= 150000:
                true_flag.value = True
        for i in range(len(arr)):
            arr[i] = arr[i] * 2

if __name__ == "__main__":
    num = Value('d', 0.0)      # 'd' — double (число с запятой)
    arr = Array('i', [1, 2, 3]) # 'i' — integer (массив целых чисел)
    true_flag = Value('b', False)
    lock = Lock()

    processes = [Process(target=update_data, args=(num, arr, lock, true_flag)) for _ in range(10)]
    for p in processes: p.start()
    for p in processes: p.join()

    print(f"Число: {num.value}")
    print(f"Массив: {arr[:]}")
    print(f"True flag: {true_flag.value}")