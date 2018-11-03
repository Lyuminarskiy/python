"""
**Задание 2.4. Калькулятор дробей.**

Запросить у пользователя два числа в виде ``12#3/5``, где до знака ``#`` идёт целая часть,
между ``#`` и ``/`` идёт числитель, после ``/`` идёт знаменатель и операция.
Вывести результат в аналогичном виде.

Пример работы::

    Первое число (a#b/c): -2#1/2
    Второе число (a#b/c): 1#1/3
    Операция (+-*/): +
    Результат: -2#1/2 + 1#1/3 = -1#1/6
"""

import re
from fractions import Fraction
from task_1_1 import calculate


def fraction_from_string(representation: str) -> Fraction:
    """
    На основе строкового представления дроби создаёт объект типа ``Fraction``.

    Строковое представление - строка формата ``a#b/c``, где:

    * ``a`` - целая часть,
    * ``b`` - числитель,
    * ``c`` - знаменатель.

    :param representation: Строковое представление дроби.
    :return: Объект типа `Fraction``.
    """

    integer, numerator, denominator = [int(part) for part in re.split("[#/]", representation)]

    if denominator == 0:
        raise ValueError("Знаменатель дроби не может быть равен нулю")

    sign = -1 if representation[0] == "-" else 1

    return Fraction(sign * (abs(integer) * denominator + numerator), denominator)


def fraction_to_string(fraction: Fraction) -> str:
    """
    Возвращает строковое представление дроби.

    Строковое представление - строка формата ``a#b/c``, где:

    * ``a`` - целая часть,
    * ``b`` - числитель,
    * ``c`` - знаменатель.

    :param fraction: Объект типа `Fraction``.
    :return: Строковое представление дроби.
    """

    integer = int(abs(fraction.numerator) / fraction.denominator)
    numerator = abs(fraction.numerator) - integer * fraction.denominator

    sign = "" if fraction.numerator >= 0 else "-"

    return f"{sign}{integer}#{numerator}/{fraction.denominator}"


# Переопределяем формат отображения дроби.
Fraction.__str__ = fraction_to_string


if __name__ == "__main__":
    first = fraction_from_string(input("Первое число (a#b/c): "))
    second = fraction_from_string(input("Второе число (a#b/c): "))
    operation = input("Операция (+-*/): ")

    print(f"Результат: {calculate(first, second, operation)}")
