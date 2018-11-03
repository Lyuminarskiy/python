"""
Тесты для задания 3.2.
"""

from unittest import TestCase, main
from tasks import task_3_2


class TestRomanToDecimal(TestCase):

    def test_roman_to_decimal__CorrectArguments__ShouldReturnCorrectResult(self):
        """
        Проверяет работу с корректными данными.
        """

        data = [
            ("I",       1),
            ("II",      2),
            ("III",     3),
            ("IV",      4),
            ("V",       5),
            ("VI",      6),
            ("VII",     7),
            ("VIII",    8),
            ("IX",      9),
            ("X",       10),
            ("XI",      11),
            ("XII",     12),
            ("XIII",    13),
            ("XIV",     14),
            ("XV",      15),
            ("XX",      20),
            ("XXI",     21),
            ("XXX",     30),
            ("XL",      40),
            ("XLIV",    44),
            ("XLIX",    49),
            ("L",       50),
            ("LI",      51),
            ("LXXXIX",  89),
            ("XC",      90),
            ("XCIX",    99),
            ("C",       100),
            ("CCC",     300),
            ("CCCXCIX", 399),
            ("CD",      400),
            ("CDXCIX",  499)
        ]

        for roman_number, result in data:
            with self.subTest():
                self.assertEqual(task_3_2.roman_to_decimal(roman_number), result, f"roman_number={roman_number}")

    def test_roman_to_decimal__NumberIsOutOfRange__ShouldRaiseValueError(self):
        """
        Проверяет генерацию исключения при передаче значения, выходящего за допустимый диапазон.
        """

        data = ["D", "DX", "M"]

        for roman_number in data:
            with self.assertRaises(ValueError, msg=f'roman_number="{roman_number}"'):
                task_3_2.roman_to_decimal(roman_number)


if __name__ == "__main__":
    main(verbosity=2)
