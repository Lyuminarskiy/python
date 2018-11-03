"""
Тесты для задания 3.1.
"""

from unittest import TestCase
import task_3_1


class TestIsUnluckyTicket(TestCase):
    def test_is_unlucky_ticket__CorrectArguments__ShouldReturnCorrectResult(self):
        """
        Проверяет работу с корректными данными.
        """

        data = \
            [("123456", False),
             ("583689", True)]

        for ticket, result in data:
            with self.subTest():
                self.assertEqual(task_3_1.is_unlucky_ticket(ticket), result, f'ticket="{ticket}"')

    def test_is_unlucky_ticket__IncorrectLengthOfTicket__ShouldRaiseValueError(self):
        """
        Проверяет генерацию исключения при передаче не шестизначного билета.
        """

        with self.assertRaises(ValueError):
            task_3_1.is_unlucky_ticket("1")
