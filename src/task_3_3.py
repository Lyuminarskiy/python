"""
**Задание 3.3. Сумма убывающих чисел**

Для любого целого числа введем понимание "убывающей пары" - числа в котором цифры отсортированы в порядке убывания.
Например, для числа ``71801`` убывающей парой будет ``87110``.
Нужно запросить у пользователя два целых числа и вывести сумму убывающих чисел в диапазоне.
"""


def to_decreasing_number(number: int) -> int:
    """
    Преобразует число в убывающее.

    :param number: Число.
    :return: Убывающее число.
    """

    sign = 1 if number >= 0 else -1
    decreasing_number = int("".join(sorted(str(abs(number)), reverse=True)))

    return decreasing_number * sign


if __name__ == "__main__":
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))

    result = sum([to_decreasing_number(number) for number in range(start, end + 1)])
    print(f"Сумма убывающих чисел в диапазоне: {result}")
