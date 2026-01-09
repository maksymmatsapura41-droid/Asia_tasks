from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == "__main__":
    with Pool(4) as p:
        results = p.map(square, [1, 2, 3, 4, 5])
    print(results)
