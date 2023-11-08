import re

car_numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_car_numbers = re.findall(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', car_numbers)
taxi_car_numbers = re.findall(r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', car_numbers)

print("Список номеров частных автомобилей:", private_car_numbers)
print("Список номеров такси:", taxi_car_numbers)
