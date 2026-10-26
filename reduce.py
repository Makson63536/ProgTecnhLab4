_MISSING = object()


def my_reduce(function, iterable, initial=_MISSING):
    """Последовательно сворачивает iterable в одно значение."""
    iterator = iter(iterable)

    if initial is _MISSING:
        try:
            accumulator = next(iterator)
        except StopIteration:
            raise TypeError(
                "my_reduce() нельзя применить к пустой "
                "последовательности без начального значения"
            ) from None
    else:
        accumulator = initial

    for item in iterator:
        accumulator = function(accumulator, item)

    return accumulator


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    total = my_reduce(lambda a, b: a + b, numbers)
    product = my_reduce(lambda a, b: a * b, numbers)
    total_with_initial = my_reduce(
        lambda a, b: a + b,
        numbers,
        10,
    )

    print("Числа:", numbers)
    print("Сумма:", total)
    print("Произведение:", product)
    print("Сумма с начальным значением 10:", total_with_initial)
