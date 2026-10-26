def filter_even(numbers):
    """Возвращает список чётных чисел."""
    return list(filter(lambda number: number % 2 == 0, numbers))


if __name__ == "__main__":
    numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
    print("Исходный список:", numbers)
    print("Чётные числа:", filter_even(numbers))
