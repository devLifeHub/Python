class Property:
    def __init__(self, worth):
        self.worth = worth

    def calculate_tax(self):
        raise NotImplementedError("Подклассы должны реализовать этот метод.")


class Apartment(Property):
    def calculate_tax(self):
        return self.worth / 1000


class Car(Property):
    def calculate_tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def calculate_tax(self):
        return self.worth / 500


money = float(input("Введите количество ваших денег: "))

apartment_worth = float(input("Введите стоимость вашей квартиры: "))
car_worth = float(input("Введите стоимость вашей машины: "))
country_house_worth = float(input("Введите стоимость вашей дачи: "))

apartment = Apartment(apartment_worth)
car = Car(car_worth)
country_house = CountryHouse(country_house_worth)

total_tax = apartment.calculate_tax() + car.calculate_tax() + country_house.calculate_tax()

if money >= total_tax:
    print('Ваш налог составляет {} денег. У вас достаточно средств.'.format(total_tax))
else:
    lack = total_tax - money
    print('Ваш налог составляет {} денег. Вам не хватает {}.'.format(total_tax, lack))
