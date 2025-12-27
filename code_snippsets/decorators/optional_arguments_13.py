import functools

def repeat_decor(_func=None, *, repeat=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(repeat):
                result = func(*args, **kwargs)
            return result
        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)


@repeat_decor(repeat=5)
def api_request():
    print('api request')

api_request()