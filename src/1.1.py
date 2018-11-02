"""
Необходимо запросить у пользователя два числа и операцию.
В качестве операций вводятся символы +, -, *, /.
Нужно вывести результат вычислений.
"""

while True:
    first = float(input("Первое число: "))
    second = float(input("Второе число: "))
    operation = input("Операция: ")

    template = "{:.2f}"

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
