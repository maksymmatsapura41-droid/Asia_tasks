from multiprocessing import Process, Queue

def worker(name, q):
    result = f"Hello from {name}"
    q.put(result)

if __name__ == "__main__":
    q1 = Queue()
    q2 = Queue()

    p1 = Process(target=worker, args=("Process 1", q1))
    p2 = Process(target=worker, args=("Process 2", q2))

    p1.start()
    p2.start()

    print(q1.get())
    print(q2.get())

    p1.join()
    p2.join()
