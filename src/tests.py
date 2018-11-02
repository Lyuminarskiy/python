from unittest import TestCase
from src import \
    task_1_1, task_1_2, task_1_3, \
    task_2_1, task_2_2, task_2_3, task_2_4


class TestTask11(TestCase):
    def test_calculate(self):
        self.assertEqual(task_1_1.calculate(2, 3, "+"), 5)


class TestTask12(TestCase):
    def test_create_multiplication_table(self):
        self.assertEqual(task_1_2.create_multiplication_table(),
                         ("     2  3  4  5  6  7  8  9\n"
                          "  2  4  6  8 10 12 14 16 18\n"
                          "  3  6  9 12 15 18 21 24 27\n"
                          "  4  8 12 16 20 24 28 32 36\n"
                          "  5 10 15 20 25 30 35 40 45\n"
                          "  6 12 18 24 30 36 42 48 54\n"
                          "  7 14 21 28 35 42 49 56 63\n"
                          "  8 16 24 32 40 48 56 64 72\n"
                          "  9 18 27 36 45 54 63 72 81\n"))
