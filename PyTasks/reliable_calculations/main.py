import math


def get_safe_sqrt(num):
    try:
        if not isinstance(num, (int, float)):
            raise TypeError("Введенное значение не является числом.")
        if num < 0:
            raise ValueError("Отрицательное число. Квадратный корень не определен.")
        return math.sqrt(num)
    except (ValueError, TypeError) as e:
        return str(e)


numbers = [16, 25, -9, 0, 4.5, "abc"]

for number in numbers:
    result = get_safe_sqrt(number)
    print(f"Квадратный корень из {number}: {result}")
