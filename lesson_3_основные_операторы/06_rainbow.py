# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)
sd.get_point(10, 10)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

for i in range(0, 31, 5):
    sd.line(sd.get_point(50 + i, 50), sd.get_point(350 + i, 450), width=4, color=rainbow_colors[i // 5])
    print(i)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

for i in range(0, 62, 10):
    sd.circle(sd.get_point(0, 0), 100 + i, width=10, color=rainbow_colors[i // 10])
sd.pause()
