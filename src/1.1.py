"""
Задание 1.1. Калькулятор v1

Необходимо запросить у пользователя два числа и операцию.
В качестве операций вводятся символы +, -, *, /.
Нужно вывести результат вычислений.
"""

first = float(input("Первое число: "))
second = float(input("Второе число: "))
operation = input("Операция (+-*/): ")

template = "Результат: {:.2f}"

if operation == "+":
    print(template.format(first + second))
elif operation == "-":
    print(template.format(first - second))
elif operation == "*":
    print(template.format(first * second))
elif operation == "/":
    if second == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо")
    else:
        print(template.format(first / second))
else:
    raise ValueError("Неизвестная операция")
