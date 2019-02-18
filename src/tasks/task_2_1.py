"""
**Задание 2.1. Разворот слов в предложении**

Запросить у пользователя предложение без знаков препинания и вывести строку с развернутыми словами.

Пример работы::

    Введите предложение: Кота манит ток
    Разворот по словам: атоК тинам кот
"""


def reverse_words(sentence: str) -> str:
    """
    Разворачивает слова в предложении без знаков препинания.

    :param sentence: Предложение.
    :return: Результат преобразования.
    """
    return " ".join([word[::-1] for word in sentence.split()])


if __name__ == "__main__":
    sentence = input("Введите предложение: ")
    print(f"Разворот по словам: {reverse_words(sentence)}")