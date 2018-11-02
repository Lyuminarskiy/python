"""
Задание 1.1. Калькулятор v1

Необходимо запросить у пользователя два числа и операцию.
В качестве операций вводятся символы +, -, *, /.
Нужно вывести результат вычислений.
"""

template = "Результат: {:.2f}"

while True:
    first = float(input("Первое число: "))
    second = float(input("Второе число: "))
    operation = input("Операция: ")

    if operation == "+":
        print(template.format(first + second))
    elif operation == "-":
        print(template.format(first - second))
    elif operation == "*":
        print(template.format(first * second))
    elif operation == "/":
        if second == 0:
            print("Деление на ноль недопустимо")
        else:
            print(template.format(first / second))
    else:
        print("Неизвестная операция")

    print()
