'''
Напишите декоратор retry(times), который повторяет выполнение 
функции при возникновении исключения.
times - количество попыток.
Если все попытки неудачны, декоратор выбрасывает последнее исключение.
Реализуйте возможность использовать декоратор без передачи аргументов.'''

import functools

def retry(_func=None, *, times=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_error = None 
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f'The error happend, retrying {i} of {times}')
                    func_error = e
            raise func_error
        return wrapper
    if _func is None:
        return decorator
    else:
        return decorator(_func)

# @retry(times=3)
@retry
def risky_action():
    import random
    if random.random() < 0.7:
        raise ValueError("Error!")
    return "Success!"

print(risky_action())
