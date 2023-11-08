from typing import Callable
from functools import wraps

app = dict()


def callback(route: str) -> Callable:
    """
    Декоратор для связывания функций обратного вызова с маршрутами
    --> route - маршрут, к которому будет привязана функция обратного вызова
    """

    def decorator_callback(name_function: Callable) -> Callable:
        """ Декоратор функции обратного вызова """
        app[route] = name_function

        @wraps(name_function)
        def wrapper(*args, **kwargs):
            function_call = name_function(*args, **kwargs)
            return function_call

        return wrapper

    return decorator_callback


@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
