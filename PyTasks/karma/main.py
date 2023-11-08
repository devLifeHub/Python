import random
import os

class KillError(Exception):
    def __str__(self):
        return 'Событие, связанное с убийством или смертью'


class DrunkError(Exception):
    def __str__(self):
        return 'Событие, связанное с пьянством или алкогольными проблемами'


class CarCrashError(Exception):
    def __str__(self):
        return 'Событие, связанное с происхождением автомобильной аварии'


class GluttonyError(Exception):
    def __str__(self):
        return 'Событие, связанное с перееданием или впаданием в чрезмерное обжорство'


class DepressionError(Exception):
    def __str__(self):
        return 'Событие, связанное с попаданием в депрессию или психологические проблемы'


class KarmaSimulator:
    def __init__(self):
        self.__karma = 0

    def one_day(self):
        karma_points = random.randint(1, 7)
        self.__karma += karma_points

        if random.random() < 0.1:
            random_error = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
            raise random_error

    def get_karma(self):
        return self.__karma

simulator = KarmaSimulator()
res_karma = 500
os.remove("karma.log") if os.path.exists("karma.log") else None

while simulator.get_karma() < res_karma:
    try:
        simulator.one_day()
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as error:
        with open("karma.log", "a") as log_file:
            log_file.write('Произошло: {}\n'.format(error))

print('Просветление достигнуто! Поздравляем!')
