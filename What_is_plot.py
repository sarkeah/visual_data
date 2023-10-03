import matplotlib.pyplot as plt

val_len = int(input())  # Максимальное число, до которого будут высчитываться квадраты и рисоваться график
values, squares = [], []

for val in range(1, val_len+1):  # Заполнение списков значениями и их квадратами
    values.append(val)
    squares.append(val**2)

plt.plot(values, squares, linewidth=6)  # Линия графика
plt.title('Squares', fontsize=25)  # Название графика
plt.xlabel('Values', fontsize=15)  # Название оси x
plt.ylabel('Squares of values', fontsize=15)  # Название оси y
plt.tick_params(axis='both', labelsize=15)
plt.show()
