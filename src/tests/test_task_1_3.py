"""
Тесты для задания 1.3.
"""

from unittest import TestCase
import task_1_3


class TestIsTriangle(TestCase):

    def test_is_triangle__CorrectArguments__ShouldReturnCorrectResult(self):
        """
        Проверяет работу с корректными данными.
        """

        data = \
            [(-1, False),
             ( 0, True),
             ( 1, True),
             ( 2, False),
             ( 3, True),
             ( 4, False),
             ( 5, False),
             ( 6, True)]

        for value, result in data:
            with self.subTest():
                self.assertEqual(task_1_3.is_triangle(value), result, f"value={value}")
