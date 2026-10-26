from functools import wraps
from time import perf_counter


def measure_time(func):
    """Измеряет время функции"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start

        print( f"Время выполнения:{elapsed: .6f} с")
        return result

    return wrapper


@measure_time
def hello_world():
    print("Hello World!")


if __name__ == "__main__":
    hello_world()
