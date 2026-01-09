def do_twice(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        value_1 = func(*args, **kwargs)
        return value, value_1
    return wrapper


@do_twice
def return_greeting(name):
     print("Creating greeting")
     return f"Hi {name}"

print(return_greeting("Alex"))