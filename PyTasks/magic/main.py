class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        else:
            return None


class Earth:
    def __str__(self):
        return 'Огонь'


class Storm:
    def __str__(self):
        return 'Шторм'


class Vapor:
    def __str__(self):
        return 'Пар'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Lightning:
    def __str__(self):
        return 'Молния'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


water = Water()
air = Air()
fire = Fire()
earth = Earth()

storm = water + air
vapor = water + fire
dirt = water + earth
lightning = air + fire
dust = air + earth
lava = fire + earth

print(storm)
print(vapor)
print(dirt)
print(lightning)
print(dust)
print(lava)
