import matplotlib.pyplot as plt
from RandomWalk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
plt.figure(figsize=(10, 6))
point_nums = list(range(rw.num_points))
plt.gca().get_yaxis().get_major_formatter().set_scientific(False)  # Отключение "смещения"
plt.scatter(rw.y_values, rw.x_values, c=point_nums, cmap=plt.cm.Purples, edgecolors='None', s=15)  # Все точки на график
plt.scatter(0, 0, c='green', edgecolors='None', s=100)  # Первая точка увеличена и окрашена в зелёный
plt.scatter(rw.y_values[-1], rw.x_values[-1], c='red', edgecolors='None', s=100)  # Последняя точка -> красный и больше
plt.tick_params(axis='both', which='minor', labelsize=15)  # Цвет точек тускнеет в порядке добавления
plt.show()
