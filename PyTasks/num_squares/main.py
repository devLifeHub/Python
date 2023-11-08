from typing import Iterator


# Класс-итератор
class SquaresIterator:
    def __init__(self, num: int):
        self.num = num
        self.current = 1

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.current <= self.num:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration


number = int(input("Введите число N: "))
squares = SquaresIterator(number)

for square in squares:
    print(square)


# Функция-генератор
def generate_squares(n: int) -> Iterator[int]:
    for i in range(1, n + 1):
        yield i ** 2


number = int(input("Введите число N: "))
squares = generate_squares(number)

for square in squares:
    print(square)

# Генераторное выражение
input_num = int(input("Введите число N: "))
squares = (i ** 2 for i in range(1, input_num + 1))

for square in squares:
    print(square)
