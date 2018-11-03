"""
**Задание 1.3. Треугольные числа.**

Проверить является ли введенное пользователем число `треугольным <https://ru.wikipedia.org/wiki/Треугольное_число>`_.
"""

from math import sqrt


def is_triangle(value: int) -> bool:
    """
    Проверяет, является ли число треугольным.

    :param value: Проверяемое число.
    :return: Результат проверки.
    """
    return value >= 0 and sqrt(value * 8 + 1).is_integer()


if __name__ == "__main__":
    number = int(input("Введите число: "))

    if is_triangle(number):
        print("Введено треугольное число")
    else:
        print("Введённое число не является треугольным")
