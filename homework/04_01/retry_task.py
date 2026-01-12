'''
Напишите декоратор retry(times), который повторяет выполнение 
функции при возникновении исключения.
times - количество попыток.
Если все попытки неудачны, декоратор выбрасывает последнее исключение.
Реализуйте возможность использовать декоратор без передачи аргументов.'''

import functools

def retry(times=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f'The error happend, retrying {i} of {times}')
                    func_error = e
            return func_error
        return wrapper
    return decorator

@retry(times=3)
def risky_action():
    import random
    if random.random() < 0.7:
        raise ValueError("Error!")
    return "Success!"

print(risky_action())
