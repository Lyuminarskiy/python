"""
Тесты для задания 2.4.
"""

from unittest import TestCase, main
from fractions import Fraction
from tasks import task_2_4


class TestFractionFromString(TestCase):

    def test_fraction_from_string__CorrectArguments__ShouldReturnCorrectResult(self):
        """
        Проверяет работу с корректными данными.
        """

        data = [
            ("-2#1/2", Fraction(-5, 2)),
            ( "1#1/3", Fraction( 4, 3)),
            ("-1#1/6", Fraction(-7, 6)),
            ( "0#1/7", Fraction( 1, 7)),
            ("-0#1/7", Fraction(-1, 7))
        ]

        for representation, result in data:
            with self.subTest():
                self.assertEqual(task_2_4.fraction_from_string(representation), result,
                                 f'representation="{representation}"')

    def test_fraction_from_string__DenominatorIsZero__ShouldRaiseValueError(self):
        """
        Проверяет генерацию исключения при передаче нулевого знаменателя.
        """

        with self.assertRaises(ValueError):
            task_2_4.fraction_from_string("1#1/0")


class TestFractionToString(TestCase):

    def test_fraction_to_string__CorrectArguments__ShouldReturnCorrectResult(self):
        """
        Проверяет работу с корректными данными.
        """

        data = \
            [(Fraction(-5, 2), "-2#1/2"),
             (Fraction(4, 3), "1#1/3"),
             (Fraction(-7, 6), "-1#1/6"),
             (Fraction(1, 7), "0#1/7"),
             (Fraction(-1, 7), "-0#1/7")]

        for fraction, result in data:
            with self.subTest():
                self.assertEqual(task_2_4.fraction_to_string(fraction), result, f"fraction={fraction}")


if __name__ == "__main__":
    main(verbosity=2)
