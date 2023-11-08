import random


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, opponent):
        damage = 20
        opponent.health -= damage
        print(
            '{name} атакует {opp_name}. {opp_name} осталось {opp_health} здоровья.'.format(
                name=self.name,
                opp_name=opponent.name,
                opp_health=opponent.health
            ))
    def is_alive(self):
        return self.health > 0



class Battle:
    def __init__(self, warr1, warr2):
        self.warrior1 = warr1
        self.warrior2 = warr2

    def start_battle(self):
        while self.warrior1.is_alive() and self.warrior2.is_alive():
            attacker, defender = random.sample([self.warrior1, self.warrior2], 2)
            attacker.attack(defender)

        if self.warrior1.health <= 0:
            print('{} одержал победу!'.format(self.warrior1.name))
        else:
            print('{} одержал победу!'.format(self.warrior2.name))


warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

battle = Battle(warrior1, warrior2)
battle.start_battle()
