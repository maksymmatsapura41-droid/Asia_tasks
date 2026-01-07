class Repeat:
    def __init__(self, times=1):
        self.times = times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                func(*args, **kwargs)
        return wrapper


@Repeat()
def greet(name):
    print(f"Hi, {name}!")

greet("John")

# repeat_instance = Repeat(times=3)     # __init__
# greet = repeat_instance.__call__(greet)
