import functools
from typing import Callable


def how_are_you(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        input("Как дела? ")
        print("А у меня не очень!")
        return func(*args, **kwargs)

    return wrapper


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


test()
