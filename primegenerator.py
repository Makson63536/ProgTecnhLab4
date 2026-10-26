from math import floor


def primegenerator(limit):
    """Генерирует простые числа до limit включительно."""
    for number in range(2, limit + 1):
        for divisor in range(2, floor(number**(1/2)) + 1):
            if number % divisor == 0:
                break
        else:
            yield number


if __name__ == "__main__":
    limit = int(input("Введите верхнюю границу: "))
    primes = list(primegenerator(limit))
    print("Простые числа:", primes)
