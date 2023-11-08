import time
from datetime import datetime


def timer(cls, func, date_format):
    def wrapped(*args, **kwargs):
        format = date_format
        for sym in format:
            if sym.isalpha():
                format = date_format.replace(sym, '%' + sym)

        print("Запускается '{cls_name}.{func_name}'. Дата и время запуска: {datetime}".format(
            cls_name=cls.__name__,
            func_name=func.__name__,
            datetime=datetime.now().strftime(format)
        ))
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Завершение '{cls_name}.{func_name}', время работы = {time} сек.".format(
            cls_name=cls.__name__,
            func_name=func.__name__,
            time=round(end - start, 3)
        ))
        return result

    return wrapped


def log_methods(date_format):
    def decorate(cls):
        for method in dir(cls):
            if not method.startswith('__'):
                current_method = getattr(cls, method)
                decorated_method = timer(cls, current_method, date_format)
                setattr(cls, method, decorated_method)
        return cls

    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


def test_sum_2():
    print("test sum 2")
    number = 200
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])

    return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")


my_obj = B()
my_obj.test_sum_1()
test_sum_2()
