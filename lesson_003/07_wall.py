# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (1200, 600)

# (0, 2) -> (0, 52) -> (0, 102) += 50
# (0, 52) -> (100, 52) -> (200, 52) += 100

# (0, 52) -> (52, 102) -> (102, 152)

start_point = sd.get_point(0, 2)
end_point = sd.get_point(1200, 2)
sd.line(start_point, end_point, color=sd.COLOR_GREEN, width=4)

for horizontal in range(0, 650, 50):
    start_point = sd.get_point(0, horizontal)
    end_point = sd.get_point(1200, horizontal)
    sd.line(start_point, end_point, color=sd.COLOR_GREEN, width=4)

for x in range(0, 602, 100):
    for vertical in range(-20, 1200, 100):
        start_point = sd.get_point(vertical, x)
        end_point = sd.get_point(vertical, x + 50)
        sd.line(start_point, end_point, color=sd.COLOR_GREEN, width=4)

for x in range(50, 602, 100):
    for vertical in range(30, 1200, 100):
        start_point = sd.get_point(vertical, x)
        end_point = sd.get_point(vertical, x + 50)
        sd.line(start_point, end_point, color=sd.COLOR_GREEN, width=4)

sd.pause()