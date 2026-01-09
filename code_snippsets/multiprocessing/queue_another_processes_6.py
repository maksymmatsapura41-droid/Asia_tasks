from multiprocessing import Process, Queue
import time

def producer(q):
    for i in range(5):
        item = f"data {i}"
        print(f"added: {item}")
        q.put(item)
        time.sleep(0.5)

def consumer(q, name):
    while True:
        try:
            item = q.get(timeout=2)
            print(f"{name} get: {item}")
        except:
            break

if __name__ == "__main__":
    q = Queue()

    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q, "Consumer 1"))
    p3 = Process(target=consumer, args=(q, "Consumer 2"))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
