def do_it_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper


@do_it_twice
def do_something_twice(name):
    print(f"Something is happening before the function is called. {name}")

do_something_twice("john")