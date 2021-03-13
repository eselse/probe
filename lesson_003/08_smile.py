# -*- coding: utf-8 -*-

# (определение функций)
import random
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

full_colors = (
    sd.COLOR_WHITE,
    sd.COLOR_BLACK,

    sd.COLOR_RED,
    sd.COLOR_ORANGE,
    sd.COLOR_YELLOW,
    sd.COLOR_GREEN,
    sd.COLOR_CYAN,
    sd.COLOR_BLUE,
    sd.COLOR_PURPLE,

    sd.COLOR_DARK_YELLOW,
    sd.COLOR_DARK_ORANGE,
    sd.COLOR_DARK_RED,
    sd.COLOR_DARK_GREEN,
    sd.COLOR_DARK_CYAN,
    sd.COLOR_DARK_BLUE,
    sd.COLOR_DARK_PURPLE
)
sd.resolution = (1200, 600)

def draw_smile(x, y, color):

    local_center_point = sd.get_point(x, y)
    sd.circle(local_center_point, 50, color, 4)

    left_bottom = sd.get_point(x - 21, y + 11)
    right_top = sd.get_point(x - 11, y + 21)
    sd.ellipse(left_bottom, right_top, color, 3)

    left_bottom = sd.get_point(x + 9, y + 11)
    right_top = sd.get_point(x + 19, y + 21)
    sd.ellipse(left_bottom, right_top, color, 3)

    left_bottom = sd.get_point(x - 25, y + 10)
    right_top = sd.get_point(x - 7, y + 23)
    sd.ellipse(left_bottom, right_top, color, 3)

    left_bottom = sd.get_point(x + 5, y + 10)
    right_top = sd.get_point(x + 23, y + 23)
    sd.ellipse(left_bottom, right_top, color, 3)

    start_point = sd.get_point(x - 12, y - 20)
    end_point = sd.get_point(x + 8, y - 20)
    sd.line(start_point, end_point, color, 3)

    start_point = sd.get_point(x - 12, y - 21)
    end_point = sd.get_point(x - 18, y - 15)
    sd.line(start_point, end_point, color, 4)

    start_point = sd.get_point(x + 7, y - 21)
    end_point = sd.get_point(x + 13, y - 15)
    sd.line(start_point, end_point, color, 4)


# draw_smile(600, 300, sd.COLOR_GREEN)
# sd.pause()

for num in range(0, 10):
    random_color = random.randint(0, len(full_colors)-1)
    random_x = random.randint(100, 1100)
    random_y = random.randint(100, 500)
    draw_smile(random_x, random_y, full_colors[random_color])
sd.pause()