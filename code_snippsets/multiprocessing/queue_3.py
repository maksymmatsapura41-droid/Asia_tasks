from multiprocessing import Process, Queue

def worker(q, num):
    # unique process
    q.put(f"Процесс {num} завершён")

def print_res(list_of_res):
    for l in list_of_res:
        print(l)

if __name__ == "__main__":
    q = Queue()
    processes = [Process(target=worker, args=(q, i)) for i in range(7)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    # main process
    res = []
    while not q.empty():
        res.append(q.get())

    p_1 = Process(target=print_res, args=(res,))
    p_1.start()
    p_1.join()


