import time


class LoggerDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        print("Вызов функции {}".format(self.func.__name__))
        print("Аргументы: {}, {}".format(args, kwargs))
        print("Результат: {}".format(result))
        print("Время выполнения: {} секунд".format(execution_time))

        return result


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)
