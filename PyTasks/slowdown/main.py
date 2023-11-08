import functools
import time
from typing import Callable


def slowdown_func(sec: int) -> Callable:
    def decor_func(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrap_func(*args, **kwargs):
            time.sleep(sec)
            return func(*args, **kwargs)
        return wrap_func
    return decor_func


@slowdown_func(2)
def test() -> None:
    print('<Тут что-то происходит...>')


test()
