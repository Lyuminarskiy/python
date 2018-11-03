"""
Задание 3.2. Римский ужас.

Пользователь вводит римское число меньше 500. Нужно вывести его привычное десятичное представление.

https://ru.wikipedia.org/Римские_цифры
"""

roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}


def roman_to_decimal(roman: str) -> int:
    """
    Преобразует римское число меньше 500 в десятичное.

    :param roman: Римское число.
    :return: Десятичное число.
    """

    if not all([numeral in roman_numerals for numeral in roman]) or roman.startswith("D"):
        raise ValueError("Римское число должно быть меньше 500")


if __name__ == "__main__":
    roman = input("Введите римское число: ")

    print(f"Десятичное представление: {roman_to_decimal(roman)}")
