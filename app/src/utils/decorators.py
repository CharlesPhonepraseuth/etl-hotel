# Standard library imports
import time


def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print(f'{func.__name__} finished in {round(end - start, 2)} second(s)')

        return result
    return wrapper
