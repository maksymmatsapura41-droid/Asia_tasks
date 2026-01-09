# Задание 1:
# Создать декоратор, который при вызове функции печатает все её аргументы.
def print_args(function):
    def wrapper(*args, **kwargs):
        print(*args, **kwargs)
        return function(*args, **kwargs)
    return wrapper

# Задание 2:
# Создать декоратор, который превращает строку, возвращаемую функцией, в заглавные буквы.
def make_uppercase(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs).upper()
    return wrapper

# Задание 3:
# Декоратор проверяет, что все числовые аргументы функции положительные.
# Если есть неположительные - выбрасывает ValueError.
def validate_type(function):
    def wrapper(*args, **kwargs):
        for a in list(args) + list(kwargs.values()):
            if isinstance(a, (int, float)) and a < 0:
                raise ValueError
        return function(*args, **kwargs)
    return wrapper


@make_uppercase
@print_args
@validate_type
def return_string(input_string: str, num: int):
    return input_string

print(return_string('abcdIfz', 3))