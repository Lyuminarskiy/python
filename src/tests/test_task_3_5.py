"""
Тесты для задания 3.4.
"""

from unittest import TestCase
import task_3_5


class TestToSymmetricTernaryNumber(TestCase):

    def test_to_symmetric_ternary_number__CorrectArguments__ShouldReturnCorrectResult(self):
        """
        Проверяет работу с корректными данными.
        """

        data = [
            (-5, "-++"),
            (-4,  "--"),
            (-3,  "-0"),
            (-2,  "-+"),
            (-1,   "-"),
            ( 0,   "0"),
            ( 1,   "+"),
            ( 2,  "+-"),
            ( 3,  "+0"),
            ( 4,  "++"),
            ( 5, "+--"),
            ( 6, "+-0"),
            ( 7, "+-+"),
            ( 8, "+0-"),
            ( 9, "+00"),
            (10, "+0+"),
            (11, "++-"),
            (12, "++0")
        ]

        for number, result in data:
            with self.subTest():
                self.assertEqual(task_3_5.to_symmetric_ternary_number(number), result, f"number={number}")


class TestFromSymmetricTernaryNumber(TestCase):

    def test_from_symmetric_ternary_number__CorrectArguments__ShouldReturnCorrectResult(self):
        """
        Проверяет работу с корректными данными.
        """

        data = [
            ("-++", -5),
            ( "--", -4),
            ( "-0", -3),
            ( "-+", -2),
            (  "-", -1),
            (  "0",  0),
            (  "+",  1),
            ( "+-",  2),
            ( "+0",  3),
            ( "++",  4),
            ("+--",  5),
            ("+-0",  6),
            ("+-+",  7),
            ("+0-",  8),
            ("+00",  9),
            ("+0+", 10),
            ("++-", 11),
            ("++0", 12)
        ]

        for ternary_number, result in data:
            with self.subTest():
                self.assertEqual(task_3_5.from_symmetric_ternary_number(ternary_number), result,
                                 f'ternary_number="{ternary_number}"')
