# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(600, 300)


# radius = 50
# for _ in range(3):
#     radius += 25
#     sd.circle(center_position=point, color=(200, 100, 50), radius=radius)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, color, step):
    radius = 20
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, color=color, radius=radius, width=2)
#
#
# point = sd.get_point(300, 300)
# bubble(point=point, step=10)

# Нарисовать 10 пузырьков в ряд
# for x in range(100, 1100, 100):
#     point = sd.get_point(x, 300)
#     bubble(point=point, step=10)
# Нарисовать три ряда по 10 пузырьков
# for y in range(150, 450, 100):
#     for x in range(150, 1150, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    step = random.randint(1, 30)
    bubble(point=point, color=color, step=step)

sd.pause()
