import random

class House:
    def __init__(self, food, money):
        self.food = food
        self.money = money


class Human:
    def __init__(self, name, house, satiety):
        self.name = name,
        self.house = house
        self.satiety = satiety

    def eat(self,add_satiety, remove_food):
        self.satiety += add_satiety
        self.house.food -= remove_food

    def work(self, remove_satiety, add_money):
        self.satiety -= remove_satiety
        self.house.money += add_money

    def play(self, remove_satiety):
        self.satiety -= remove_satiety

    def shopping(self, add_food, remove_money):
        self.house.food += add_food
        self.house.money -= remove_money

    def one_day(self):
        cube_num = random.randint(1, 6)
        if self.satiety < 20:
            self.eat(10, 10)
            print('Покушал! "Сытость": {satiety}, "Денег": {money}'.format(
                satiety=self.satiety,
                money=house.money
            ))
        elif house.food < 10:
            self.shopping(10, 10)
            print('Купил продукты! "Пищи": {food}, "Денег": {money}'.format(
                food=house.food,
                money=house.money
            ))
        elif house.money < 50:
            self.work(10, 10)
            print('Сходил на работу! "Сытость": {satiety}, "Денег": {money}'.format(
                satiety=self.satiety,
                money=house.money
            ))
        elif cube_num == 1:
            self.work(10, 10)
            print('Кубик показал число {num} нужно "Поработать!" - "Сытость": {satiety}, "Денег": {money}'.format(
                num=cube_num,
                satiety=self.satiety,
                money=house.money
            ))
        elif cube_num == 2:
            self.eat(10, 10)
            print('Кубик показал число {num} нужно "Поесть" - "Сытость": {satiety}, "Пищи": {food}'.format(
                num=cube_num,
                satiety=self.satiety,
                food=house.food
            ))
        else:
            self.play(10)
            print('Кубик показал число {num} нужно "Поиграть" - "Сытость": {satiety}'.format(
                num=cube_num,
                satiety=self.satiety
            ))



house = House(50, 0)
human1 = Human('Виктор', house, 50)
human2 = Human('Петя', house, 50)


for day in range(365):
    print('День {day}:'.format(day=day + 1))
    human1.one_day()
    human2.one_day()
    if human1.satiety < 0 or human2.satiety < 0:
        print("Кто-то умер от голода.")
        break
