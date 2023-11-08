from math import pi


class MyMath:
    """
    MyMath - класс, для математических вычислений.

    Методы:
    circle_len - вычисление длины окружности.
    circle_sq - вычисление площади окружности.
    cube_volume - вычисление объёма куба.
    sphere_surface_area - вычисление площади поверхности сферы.
    """
    @classmethod
    def circle_len(cls, radius: float) -> float:
        return 2 * pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        return pi * radius ** 2

    @classmethod
    def cube_volume(cls, side_length: float) -> float:
        return side_length ** 3

    @classmethod
    def sphere_surface_area(cls, radius: float) -> float:
        return 4 * pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
