from multiprocessing import Process
import os

def worker(name):
    print(f"Process {name} launched with PID {os.getpid()}")

if __name__ == "__main__":
    p = Process(target=worker, args=("A",))
    p.start()  # process start
    p.join()   # wait process finish
