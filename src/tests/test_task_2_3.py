"""
Тесты для задания 2.3.
"""

from unittest import TestCase
import task_2_3


class TestFindLongestWord(TestCase):

    def test_find_longest_word__CorrectArguments__ShouldReturnCorrectResult(self):
        """
        Проверяет работу с корректными данными.
        """

        data = [
            ("Мама мыла раму",       "раму"),
            ("Кота манит ток",       "манит"),
            ("Завтра идем купаться", "купаться")
        ]

        for sentence, result in data:
            with self.subTest():
                self.assertEqual(task_2_3.find_longest_word(sentence), result, f'sentence="{sentence}"')
