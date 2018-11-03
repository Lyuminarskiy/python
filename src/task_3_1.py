"""
**Задание 3.1. Дружные несчастные.**

Назовем автобусный билет несчастливым, если сумма цифр его шестизначного номера делится на 13.
Могут ли два идущих подряд билета оказаться несчастливыми?
"""


def is_unlucky_ticket(ticket: str) -> bool:
    """
    Проверяет, является ли шестизначный номер билета несчастливым.
    Номер билета является несчастливым, если сумма его цифр делится на 13 без остатка.

    :param ticket: Шестизначный номер билета.
    :return: Результат проверки.
    """

    if len(ticket) != 6:
        raise ValueError("Номер билета должен быть шестизначным")

    return sum([int(number) for number in ticket]) % 13 == 0


if __name__ == "__main__":
    ticket = input("Введите номер билета: ")

    if is_unlucky_ticket(ticket):
        print("Введённый несчастливый номер")
    else:
        print("Введён счастливый номер")

    for ticket, next_ticket in [(f"{number:06d}", f"{number + 1:06d}") for number in range(999999)]:
        if is_unlucky_ticket(ticket) and is_unlucky_ticket(next_ticket):
            print(f"Билеты {ticket} и {next_ticket} являются несчастливыми")
