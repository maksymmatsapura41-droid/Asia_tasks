'''
class realization
Напишите декоратор retry(times), который повторяет выполнение 
функции при возникновении исключения.
times - количество попыток.
Если все попытки неудачны, декоратор выбрасывает последнее исключение.
Реализуйте возможность использовать декоратор без передачи аргументов.'''

import functools

class Retry:
    def __init__(self, func=None, *, times=3):
        self.times = times
        self.func = func
        self.is_wrapped = func is not None # means @Retry - contains function

    def __call__(self, *args, **kwargs):
        if not self.is_wrapped:
            func = args[0]
            return Retry(func, times=self.times)
        else:
            for i in range(1, self.times + 1):
                try:
                    return self.func(*args, **kwargs)
                except Exception as e:
                    print(f'The error happend, retrying {i} of {self.times}')
                    func_error = e
            raise func_error

# @Retry(times=2)
@Retry
def risky_action():
    import random
    if random.random() < 0.7:
        raise ValueError("Error!")
    return "Success!"

print(risky_action())
