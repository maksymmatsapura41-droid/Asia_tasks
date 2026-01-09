from multiprocessing import Process

results = []

def worker(num):
    results.append(f"Process {num} finished")

processes = [Process(target=worker, args=(i,)) for i in range(3)]


if __name__ == "__main__":
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(results)
