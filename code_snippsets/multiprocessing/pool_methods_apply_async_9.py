from multiprocessing import Pool

def cube(x):
    return x ** 3

def print_result(result):
    print(f"Result: {result}")

if __name__ == "__main__":
    with Pool(1) as pool:
        res = pool.apply_async(cube, args=(3,), callback=print_result)
        res.wait()
