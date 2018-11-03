"""
Задание 1.1. Калькулятор v1.

Необходимо запросить у пользователя два числа и операцию.
В качестве операций вводятся символы +, -, *, /.
Нужно вывести результат вычислений.
"""


def calculate(first, second, operation: str):
    """
    Вычисляет арифметическую операцию `operation` над двумя числами.

    Допустимые операции:

    - `+` - сложение,
    - `-` - вычитание,
    - `*` - умножение,
    - `/` - деление.

    :param first: Первое число.
    :param second: Второе число.
    :param operation: Арифметическая операция.
    :return: Результат арифметической операции.
    """

    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        if second != 0:
            return first / second
        else:
            raise ZeroDivisionError("Деление на ноль недопустимо")
    else:
        raise ValueError("Неизвестная операция")


if __name__ == "__main__":
    first = float(input("Первое число: "))
    second = float(input("Второе число: "))
    operation = input("Операция (+-*/): ")

    print(f"Результат: {calculate(first, second)}:.2f")
