# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
sd.resolution = (1200, 600)

# color_index = 0
# for x in range(50, 80, 5):
#     start_point = sd.get_point(x, 50)
#     end_point = sd.get_point(300+x, 450)
#     sd.line(start_point, end_point, color=rainbow_colors[color_index], width=4)
#     color_index += 1
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
center_point = sd.get_point(-200, -50)
color_index = 0
for x in range(600, 880, 40):
    sd.circle(center_point, x, rainbow_colors[color_index], 40)
    color_index += 1

sd.pause()
