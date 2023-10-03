import pygal
from Dice import Dice


die = Dice()
result = []
rolls_count = 10000
for roll in range(rolls_count):
    result.append(die.roll())  # Результаты броска "куба" определённое число раз

frequencies = []
sides = []
for value in range(2, die.num_sides + 1):
    frequencies.append(result.count(value))  # Количество выпадения всех чисел
    sides.append(str(value))  # Число в виде строки

hist = pygal.Bar()
hist.title = 'Результаты броска кубика D' + str(die.num_sides) + ' ' + str(rolls_count) + ' раз.'
hist.x_labels = sides
hist.x_title = 'Грань'
hist.y_title = 'Количество выпадений'
hist.add('D' + str(die.num_sides), frequencies)
# Создание графика
hist.render_to_file('dice_frequencies.svg')  # Сохранение графика в svg файл
