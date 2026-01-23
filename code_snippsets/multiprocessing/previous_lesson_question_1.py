from multiprocessing import Process, Manager
import os

def worker(name, shared_dict):
    pid = os.getpid()
    shared_dict[pid] = f"Data from {name}"

if __name__ == "__main__":
    manager = Manager()
    shared_dict = manager.dict()

    p1 = Process(target=worker, args=("P1", shared_dict))
    p2 = Process(target=worker, args=("P2", shared_dict))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    for pid, value in shared_dict.items():
        print(f"Process {pid} returned: {value}")
