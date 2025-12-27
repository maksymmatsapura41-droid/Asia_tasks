def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@do_twice
def return_greeting(name):
     print("Creating greeting")
     return f"Hi {name}"

print(return_greeting("Alex"))