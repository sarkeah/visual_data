from random import randint


class Dice:

    def __init__(self, sides_count=6):  # Создание "куба" с заданным количеством граней
        self.num_sides = sides_count

    def roll(self):  # Получение случайного значения в пределах от 1 до количества граней куба
        return randint(1, self.num_sides)
