# -*- coding: utf-8 -*-

# (определение функций)
import random

import simple_draw as sd

sd.resolution = (1000, 1000)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def draw_smile(rand1, rand2):
    sd.circle(sd.get_point(100 + rand1, 100 + rand2), radius=50,
              color=[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
    sd.circle(sd.get_point(120 + rand1, 110 + rand2), radius=5,
              color=[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
    sd.circle(sd.get_point(80 + rand1, 110 + rand2), radius=5,
              color=[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
    sd.line(sd.get_point(100 + rand1, 100 + rand2), sd.get_point(100 + rand1, 70 + rand2), width=3,
            color=[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])


for i in range(10): draw_smile(random.randint(200, 900), random.randint(200, 900))

sd.pause()
