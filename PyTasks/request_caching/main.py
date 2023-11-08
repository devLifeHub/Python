from typing import Tuple, Union


class LRUCache:
    """
    LRUCache - класс, позволяет создавать объекты кэша с ограниченной емкостью.

    Инициализируется 3-мя параметрами:
    capacity - емкость (максимальное количество элементов).
    cache_dict - словарь для хранения ключ значение.
    used_order - массив ключей
    (для переноса на 0-ой индекс и удаление последнего элемента по ключу)

    Методы:
    get - получение по ключу элемента cache_dict,
    --> удаление элемента used_order по ключу,
    --> перенос ключа на 0-ой индекс used_order,
    --> если ключа нет, то - None

    @property cache - возвращает последний элемент
    --> если не пустой used_order, то берем последний ключ used_order
    и находим в cache_dict
    --> если пустой, то - None

    @cache.setter cache - записываем Tuple(key, value)
    --> если есть перезаписываем значение +переноса на 0-ой индекс
    --> если нет и длина >= 3, то удаляем последний и записываем новый
    --> если нет и длина < 3, то записываем

    print_cache - вывод в консоль
    """
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache_dict = {}
        self.used_order = []

    def get(self, key: str) -> Union[str, None]:
        if key in self.cache_dict:
            self.used_order.remove(key)
            self.used_order.insert(0, key)
            return self.cache_dict[key]
        else:
            return None

    @property
    def cache(self) -> Union[Tuple[str, str], None]:
        if self.used_order:
            key = self.used_order[-1]
            return key, self.cache_dict[key]
        else:
            return None

    @cache.setter
    def cache(self, new_elem: Tuple[str, str]) -> None:
        key, value = new_elem
        if key in self.cache_dict:
            self.cache_dict[key] = value
            self.used_order.remove(key)
            self.used_order.insert(0, key)
        else:
            if len(self.used_order) >= self.capacity:
                del_key = self.used_order.pop()
                del self.cache_dict[del_key]
            self.cache_dict[key] = value
            self.used_order.insert(0, key)

    def print_cache(self) -> None:
        print("LRU Cache:")
        for key in self.used_order:
            print('{} : {}'.format(key, self.cache_dict[key]))


# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
