from multiprocessing import Process

def worker(num):
    print(f"Process {num} started")

processes = []
for i in range(5):
    p = Process(target=worker, args=(i,))
    processes.append(p)


if __name__ == "__main__":
    for p in processes:
        p.start()
    for p in processes:
        p.join()
