"""
Тесты для задания 1.1.
"""

from unittest import TestCase, main
from tasks import task_1_1


class TestCalculate(TestCase):

    def test_calculate__CorrectArguments__ShouldReturnCorrectResult(self):
        """
        Проверяет работу с корректными данными.
        """

        data = [
            # Сложение
            ( 1,  5, "+",   6),
            (-3, -2, "+",  -5),

            # Вычитание
            (-3,  4, "-",  -7),
            ( 5, -3, "-",   8),

            # Умножение
            ( 3, -5, "*", -15),
            ( 1,  0, "*",   0),

            # Деление
            ( 6,  4, "/", 1.5),
            ( 0,  2, "/",   0)
        ]

        for first, second, operator, result in data:
            with self.subTest():
                self.assertEqual(task_1_1.calculate(first, second, operator), result,
                                 f'first={first}, second={second}, operator="{operator}"')

    def test_calculate__WrongOperator__ShouldRaiseValueError(self):
        """
        Проверяет генерацию исключения при передаче некорректного арифметического оператора.
        """

        with self.assertRaises(ValueError):
            task_1_1.calculate(2, 3, "\\")

    def test_calculate__DivisionByZero__ShouldRaiseZeroDivisionError(self):
        """
        Проверяет генерацию исключения при делении на ноль.
        """

        with self.assertRaises(ZeroDivisionError):
            task_1_1.calculate(1, 0, "/")


if __name__ == "__main__":
    main(verbosity=2)
