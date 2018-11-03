"""
**Задание 3.2. Римский ужас.**

Пользователь вводит `римское число <https://ru.wikipedia.org/wiki/Римские_цифры>`_ меньше ``500``.
Нужно вывести его привычное десятичное представление.


"""

import re

# Словарь для преобразования римских цифр в десятичные.
roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
# Словарь для преобразования римских чисел из вариантов для "правила вычитания" в десятичные.
roman_subtraction = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400}


def roman_to_decimal(roman_number: str) -> int:
    """
    Преобразует римское число меньше ``500`` в десятичное.

    :param roman_number: Римское число.
    :return: Десятичное число.
    """

    if not all([numeral in roman_numerals for numeral in roman_number]) or roman_number.startswith("D"):
        raise ValueError("Римское число должно быть меньше 500")

    decimal = 0

    # Обрабатываем римские числа из вариантов для "правила вычитания".
    for subtraction in roman_subtraction.items():
        # Все найденные числа удаляем из исходного.
        roman_number, number_of_subs_made = re.subn(subtraction[0], "", roman_number)
        # Преобразуем числа в десятичные.
        decimal += number_of_subs_made * subtraction[1]

    # Преобразуем все остальные римские числа.
    decimal += sum([roman_numerals[numeral] for numeral in roman_number])

    return decimal


if __name__ == "__main__":
    roman_number = input("Введите римское число: ")

    print(f"Десятичное представление: {roman_to_decimal(roman_number)}")
