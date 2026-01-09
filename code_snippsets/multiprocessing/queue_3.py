from multiprocessing import Process, Queue

def worker(q, num):
    # unique process
    q.put(f"Процесс {num} завершён")

if __name__ == "__main__":
    q = Queue()
    processes = [Process(target=worker, args=(q, i)) for i in range(7)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    # main process
    while not q.empty():
        print(q.get())
