from typing import List
from functools import reduce


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

res_floats: List[int] = list(map(lambda num: round(num**3, 3), floats))
res_names: List[str] = list(filter(lambda name: len(name) >= 5, names))
res_numbers = reduce(lambda x, y: x * y, numbers)

print(res_floats)
print(res_names)
print(res_numbers)