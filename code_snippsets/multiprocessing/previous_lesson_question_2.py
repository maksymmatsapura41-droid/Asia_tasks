from multiprocessing import Pool

def worker(x):
    return x * 2

def my_callback(result):
    print(f"Got result: {result}")

def second_callback(result):
    print(f"Got result from another process: {result}")

if __name__ == "__main__":
    with Pool(2) as pool:
        pool.apply_async(worker, args=(5,), callback=my_callback)
        pool.apply_async(worker, args=(10,), callback=second_callback)
        pool.close()
        pool.join()
