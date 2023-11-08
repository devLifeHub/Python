import functools
import datetime
from typing import Callable, Any


def logging(func: Callable) -> Any:
    @functools.wraps(func)
    def wrap_func(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print('Название функции: {}'.format(func.__name__))
            print('Документация функции: {}'.format(func.__doc__))
            return result
        except Exception as e:
            error_message = 'Функция: {name}, ошибка: {error}'.format(
                name=func.__name__, error=str(e)
            )
            with open('function_errors.log', 'a') as log:
                log.write('{date_time} --> {error}\n'.format(
                    date_time=datetime.datetime.now(),
                    error=error_message,
                ))
            print(error_message)

    return wrap_func


@logging
def test() -> None:
    """ Это простая функция, которая выводит код! """
    print('<Тут что-то происходит...>')


@logging
def test_error() -> None:
    """ Эта функция генерирует ошибку! """
    raise ValueError('Произошла ошибка')


test()
test_error()
test()
