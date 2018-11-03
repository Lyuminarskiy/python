"""
**Задание 3.4. Единцы измерения**

Составить функцию, которая позволит получать правильные окончания единиц измерения.
Можно использовать дополнительные параметры функции, не как в примере.

Пример::

    print(MyF(12,'штука')) #12 штук
    print(MyF(152,'нога')) #152 ноги
    print(MyF(0,'рубль')) #0 рублей
"""

from typing import Tuple


def pluralize(forms: Tuple[str, str, str], amount: int) -> str:
    """
    Возвращает правильную форму слова в зависимости от количества.

    Формы слова:

    #. Единственное число, именительный падеж (штука).
    #. Единственное число, родительный падеж (штуки).
    #. Множественное число, родительный падеж (штук).

    :param forms: Формы слова.
    :param amount: Количество.
    :return: Правильная форма слова.
    """

    amount = abs(amount)
    last_digit = str(amount)[-1]

    if last_digit == "1":
        return forms[0]
    elif last_digit in {"2", "3", "4"} and not 11 <= amount <= 19:
        return forms[1]
    elif last_digit in {"5", "6", "7", "8", "9", "0"}:
        return forms[2]


if __name__ == "__main__":
    forms = (input("Введите слово в ед.ч., им.пад.: "),
             input("Введите слово в ед.ч., род.пад.: "),
             input("Введите слово в мн.ч., род.пад.: "))
    amount = int(input("Введите количество: "))

    print(f"Правильная форма слова: {pluralize(forms, amount)}")
