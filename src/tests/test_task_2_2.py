"""
Тесты для задания 2.2.
"""

from unittest import TestCase
import task_2_2


class TestReverseSentence(TestCase):

    def test_reverse_sentence__CorrectArguments__ShouldReturnCorrectResult(self):
        """
        Проверяет работу с корректными данными.
        """

        data = \
            [("Мама мыла раму",       "Раму мыла мама"),
             ("Кота манит ток",       "Ток манит кота"),
             ("Завтра идем купаться", "Купаться идем завтра")]

        for sentence, result in data:
            with self.subTest():
                self.assertEqual(task_2_2.reverse_sentence(sentence), result, f'sentence="{sentence}"')
