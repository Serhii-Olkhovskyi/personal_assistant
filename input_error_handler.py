"""
Декоратор обробки помилок.
"""


def input_error(func):
    """
    A decorator for handling errors that occur due to incorrect user input.

    Параметры
    ---------
    :param func: Функция ввода от пользователя.
    :return: Вывод результата функции ввода или вывод ошибки с повторным вводом данных
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This name doesn't exist"
        except TypeError:
            return "Wrong command type"
        except IndexError:
            return "Input name and phone number"
        except ValueError as exception:
            return exception.args[0]

    return wrapper