"""
Тесты для задания 2.1.
"""

from unittest import TestCase
import task_2_1


class TestReverseWords(TestCase):

    def test_reverse_words__CorrectArguments__ShouldReturnCorrectResult(self):
        """
        Проверяет работу с корректными данными.
        """

        data = \
            [("Мама мыла раму",       "амаМ алым умар"),
             ("Кота манит ток",       "атоК тинам кот"),
             ("Завтра идем купаться", "артваЗ меди ясьтапук")]

        for sentence, result in data:
            with self.subTest():
                self.assertEqual(task_2_1.reverse_words(sentence), result, f'sentence="{sentence}"')
