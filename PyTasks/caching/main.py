def cache(func):
    cache_dict = {}

    def wrapper(*args):
        if args not in cache_dict:
            result = func(*args)
            cache_dict[args] = result
        return cache_dict[args]

    return wrapper


@cache
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и за кеширован
