from multiprocessing import Pool

def power(x, y):
    return x ** y

if __name__ == "__main__":
    with Pool(1) as pool:
        result = pool.apply(power, args=(2, 5))
    print(result)
# Blocked main process