from pathlib import Path


def filter_numbers_from_file(file_path, threshold):
    """Выдаёт числа из файла, которые больше заданного числа."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            text = line.strip()

            if not text:
                continue

            try:
                number = int(text)
            except ValueError:
                print(
                    f"Строка {line_number} пропущена: "
                    f"{text!r} — не целое число"
                )
                continue

            if number > threshold:
                yield number


if __name__ == "__main__":
    file_path = Path(__file__).resolve().parent / "numbers.txt"
    threshold = int(input("Вывести числа больше: "))

    try:
        print("Подходящие числа:")
        for number in filter_numbers_from_file(file_path, threshold):
            print(number)
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")