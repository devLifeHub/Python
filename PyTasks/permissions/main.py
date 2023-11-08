import functools
from collections.abc import Callable


def check_permission(req: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if req in list_user_permissions:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError(
                        "У пользователя недостаточно прав, чтобы выполнить функцию {}".format(func.__name__))
            except PermissionError as e:
                print("{}: {}".format(type(e).__name__, e))

        return wrapper

    return decorator


list_user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
