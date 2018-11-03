"""
Тесты для задания 3.2.
"""

from unittest import TestCase, main
from tasks import task_3_3


class TestToDecreasingNumber(TestCase):

    def test_to_decreasing_number__CorrectArguments__ShouldReturnCorrectResult(self):
        """
        Проверяет работу с корректными данными.
        """

        data = [
            ( 71801,  87110),
            (  1937,   9731),
            (     0,      0),
            ( -2038,  -8320),
            (-71801, -87110)
        ]

        for decreasing_number, result in data:
            with self.subTest():
                self.assertEqual(task_3_3.to_decreasing_number(decreasing_number), result,
                                 f"decreasing_number={decreasing_number}")


if __name__ == "__main__":
    main(verbosity=2)
