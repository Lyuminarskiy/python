"""
**Задание 1.2. Таблица Пифагора.**

Вывести таблицу Пифагора с учетом выравнивания столбцов::

       2  3  4  5  6  7  8  9
    2  4  6  8 10 12 14 16 18
    3  6  9 12 15 18 21 24 27
    4  8 12 16 20 24 28 32 36
    5 10 15 20 25 30 35 40 45
    6 12 18 24 30 36 42 48 54
    7 14 21 28 35 42 49 56 63
    8 16 24 32 40 48 56 64 72
    9 18 27 36 45 54 63 72 81
"""


def create_multiplication_table() -> str:
    """
    Создаёт таблицу умножения.

    :return: Таблица умножения.
    """

    multiplication_table = " " * 3

    for row in range(1, 10):
        for column in range(1, 10):
            if row == 1 and column == 1:
                continue
            multiplication_table += f"{row * column:3d}"
        multiplication_table += "\n"

    return multiplication_table


if __name__ == "__main__":
    print(create_multiplication_table())
