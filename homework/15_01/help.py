from multiprocessing import Pool

# Функция обработки
def analyze_string(s: str):
    if not isinstance(s, str):
        raise ValueError("Это не строка!")
    length = len(s)
    has_upper = any(c.isupper() for c in s)
    return f"'{s}' -> length={length}, has_upper={has_upper}"

# Callback для успешного результата
def on_success(result):
    print(f"Успех: {result}")

# Callback для ошибки
def on_error(error):
    print(f"Ошибка: {error}")

if __name__ == "__main__":
    strings = ["Hello", "world", 123, "Python", "async"]

    results = []
    async_results = []

    with Pool(processes=3) as pool:
        for s in strings:
            ar = pool.apply_async(
                analyze_string,
                args=(s,),
                callback=on_success,
                error_callback=on_error
            )
            async_results.append(ar)

        pool.close()
        pool.join()

        # Получаем результаты через get()
        for ar in async_results:
            try:
                res = ar.get(timeout=2)
                results.append(res)
            except Exception as e:
                print("Ошибка при получении результата:", e)

    print("Все обработанные результаты:", results)
